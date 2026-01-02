N,M = map(int,input().split())
MOD = 10**9+7
MAXN = N+200
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def ncr(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD
def nhr(n,r):
    return ncr(n+r-1, r)

from collections import Counter
def factorize(n):
    d = Counter()
    m = 2
    while m*m <= n:
        while n%m == 0:
            n //= m
            d[m] += 1
        m += 1
    if n > 1:
        d[n] += 1
    return d

factors = factorize(M)
ans = 1
for v in factors.values():
    n = nhr(N,v)
    ans *= n
    ans %= MOD
print(ans)