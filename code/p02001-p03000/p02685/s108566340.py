#左からn個目でendが特定の色の場合に
N,M,K = list(map(int,input().split()))

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

def pow(base, exponent, mod=1e9+7) -> int:
  if exponent == 0:
    return 1
  if exponent > 1:
    d,m = divmod(exponent, 2)
    return (base**m * pow(base, d, mod)**2 ) % mod
  else:
    return base

m = 998244353
res = 0
B = 1
if M != 1:
  mi = modinv(M-1,m)
  A = M * pow(M-1,N-1,m)
  for k in range(K+1):
    if k>0:
      B = (B*(N-k)*modinv(k,m))%m
    res = (res+ A*B)%m
    A = (A*mi)%m
  print (res)
else:
  if K == N-1:
    
    print(1)
  else:
    print(0)