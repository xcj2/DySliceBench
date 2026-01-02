n, a, b = map(int, input().split())
mod = int(1e+9) + 7
def extgcd(a, b):
  if b == 0:
    return 1, 0
  else:
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l != 0:
      x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
      k, l = l, k % l
    return x
def inved(x):
  a = extgcd(x, mod)
  return a % mod
def doubling(N, M):
  y = 1
  base = N
  while M != 0:
    if M % 2 == 1:
      y *= base
      y %= mod
    base *= base
    base %= mod
    M //= 2
  return y
S = [inved(i+1) for i in range(b)]
A = doubling(2, n)
A = (A - 1) % mod
proda, prodb = 1, 1
for i in range(a):
  proda *= ((n - i) * S[i]) % mod
  proda %= mod
for i in range(b):
  prodb *= ((n - i) * S[i]) % mod
  prodb %= mod
print((A - proda - prodb) % mod)