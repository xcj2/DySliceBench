def xgcd(a, b):
  x0, y0, x1, y1 = 1, 0, 0, 1
  while b != 0:
    q, a, b = a // b, b, a % b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
  return a, x0, y0
def modinv(a, m):
  g, x, y = xgcd(a, m)
  if g != 1:
    raise Exception('modular inverse does not exist')
  else:
    return x % m
def combination(n, k, mod=1e9+7) -> int:
  ret = 1
  for i in range(1, k+1):
    ret = (ret * (n-k+i) * modinv(i, mod))%mod
  return int(ret)

N,M = list(map(int,input().split()))

Na = combination(N,2) if N >=2 else 0
Ma = combination(M,2) if M >=2 else 0

print(Na+Ma)