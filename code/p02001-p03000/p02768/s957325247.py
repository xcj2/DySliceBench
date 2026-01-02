import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

__MAX_N = 300000
fac = [0] * __MAX_N
finv = [0] * __MAX_N
inv = [0] * __MAX_N

def combinit(m):
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, __MAX_N):
        fac[i] = fac[i - 1] * i % m
        inv[i] = m - inv[m % i] * (m // i) % m
        finv[i] = finv[i - 1] * inv[i] % m

def modpow(n, p, m):
	if p == 0:
		return 1
	if p % 2 == 0:
		t = modpow(n, p // 2, m)
		return t * t % m
	return n * modpow(n, p - 1, m) % m

def comb(n, k, m):
    if n == 0 and k == 0:
        return 1
    if n < k or n < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % m) % m

def comb2(n, k, m):
    if n == k or k == 0:
        return 1
    if n < k:
        return 0

    res = 1
    for i in range(k):
        res *= (n - i)
        res %= m
        res *= modpow(i + 1, m - 2, m)
        res %= mod
    
    return res

n, a, b = na()
ans = modpow(2, n, mod) - 1
ans -= comb2(n, a, mod)
ans -= comb2(n, b, mod)
ans %= mod
print(ans)