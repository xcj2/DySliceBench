N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

def ncr(n, r, p):
  num = den = 1
  for i in range(r):
    num = (num * (n - i)) % p
    den = (den * (i + 1)) % p
  return (num * pow(den, p - 2, p)) % p

Mod = 10**9+7
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
def COMinit():
  #N_C_kのN
  for i in range(2, N+10):
    fac.append(fac[-1]*i%Mod)
    inv.append((-inv[Mod%i] * (Mod//i)) % Mod)
    finv.append(finv[-1] * inv[-1] % Mod)


def COM(n, k):
  if n < 0 or k < 0 or n < k:
    return 0
  return fac[n] * (finv[k] * finv[n-k] % Mod) % Mod


COMinit()
p=10**9+7

ans = 0
for i in range(N-K+1):
  j = N-1-i
  #ans += A[j] * ncr(j, K-1, p)
  ans += A[j] * COM(j, K-1)
  ans %= p

for i in range(N-K+1):
  #ans -= A[i] * ncr(N-i-1, K-1, p)
  ans -= A[i] * COM(N-i-1, K-1)
  ans %= p

print(ans)