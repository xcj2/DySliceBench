M = 10 ** 9 + 7
X, Y = map(int, input().split())

def f(n):
  if n == 0: return 1
  res = 1
  for i in range(1,n+1):
    res = (res * i) % M
  return res % M

def pow(x, n):
  res = 1
  while n:
    if (n & 1) == 1:
      res = res * x % M
    x = x * x % M
    n = n >> 1
  return res

def c(n,r):
  if r == 0 or r == n:
    res = 1
  elif r == 1 :
    res = n
  else:
    res = f(n) * pow(f(r), M-2) * pow(f(n-r), M-2)
  return res % M

if (X+Y) % 3 != 0:
  ans = 0
else:
  a = 0
  b = (X+Y)//3
  if X < Y: X, Y = Y, X
  a = X - Y
  a += (2*Y-X)//3
  if 2*Y - X < 0:
    ans = 0
  else:
    ans = c(b, a) % M
print (ans)