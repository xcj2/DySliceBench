N = int(input())
def gcd(x, y):
  k, l = x, y
  while l:
    k, l = l, k % l
  return k
def factorization(n):
  a = n
  p = 2
  D = {}
  while a != 1:
    cnt = 0
    while a % p == 0:
      cnt += 1
      a //= p
    if cnt:
      D[p] = cnt
    p += 1
    if p * p > n and a != 1:
      D[a] = 1
      break
  return D
X = factorization(2*N)
F = {1}
for i in X:
  tmp = set()
  for j in F:
    tmp.add(j)
    p = j
    for k in range(X[i]):
      tmp.add(p*i)
      p *= i
  for j in tmp:
    F.add(j)
def extgcd(a, b, c):
  x, y, u, v, k, l = 1, 0, 0, 1, a, b
  while l:
    x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
  return c*x, c*y
m = 2*N+1
for i in F:
  if gcd(i, (2*N)//i) == 1:
    x, y = extgcd((2*N)//i, -i, 1)
    while x <= 0 or y <= 0:
      x += i
      y += (2*N)//i
    m = min(x*((2*N)//i), m)
print(m)