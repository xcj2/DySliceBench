import math
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
def combination(n, r, mod=10**9+7):
  r = min(r, n-r)
  res = 1
  for i in range(r):
      res = res * (n - i) * modinv(i+1, mod) % mod
  return res

def COMint():
  fac[0]=1
  fac[1]=1
  finv[0]=1
  finv[1]=1
  inv[1]=1
  for i in range(2,N+1):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD
def com(n,k):
  if n<k:
    return 0
  return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
MOD=10**9+7
#繰り返し２乗法を使う場合
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n,a,b=[int(x) for x in input().split()]
ans1 = pow(2,n,MOD)
N = n
a1=combination(n,a)
b1 = combination(n,b)
if ans1-a1%MOD-b1%MOD<0:
  print(((ans1-a1%MOD-b1%MOD)%MOD+MOD)%MOD-1)
else:
  print(ans1-a1%MOD-b1%MOD-1)
