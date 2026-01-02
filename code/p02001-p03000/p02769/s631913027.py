import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, k = na()
mod = 1000000007

def comb(n, r, mod):
    if n < 0 or r < 0 or r > n: return 0
    nu = 1
    de = 1
    for i in range(r):
        nu = nu * (n-i) % mod
        de = de * (i+1) % mod
    return nu * inv(de, mod) % mod

def inv(a, mod):
    b = mod
    p, q = 1, 0
    while b > 0:
        c = a//b
        d = a; a = b; b = d % b
        d = p; p = q; q = d-c*q
    return p+mod if p < 0 else p

# 120
# 012

# n-k個は1以上
# k+1個以上が0

def enumfif(n, mod):
    f = [0] * (n+1)
    invf = [0] * (n+1)
    f[0] = 1
    for i in range(1, n+1):
        f[i] = f[i-1] * i % mod

    a = f[n]
    b = mod
    p, q = 1, 0
    while b > 0:
        c = a//b
        d = a; a = b; b = d % b
        d = p; p = q; q = d-c*q
    invf[n] = p + mod if p < 0 else p
    for i in range(n-1,-1,-1):
        invf[i] = invf[i+1] * (i+1) % mod
    return f, invf

def C(n, r, mod, fif):
    if n < 0 or r < 0 or r > n:
        return 0
    return fif[0][n] * fif[1][r] * fif[1][n-r] % mod


if k >= n-1:
    print(comb(n-1+n, n, mod))
else:
    fif = enumfif(400005, mod)
    # sum C(n,z)*C(n-z-1+n, n, mod)
    ans = comb(n-1+n, n, mod)
    for z in range(k+1, n+1):
        ans -= C(n, z, mod, fif) * C(n-z-1+(n-(n-z)), (n-(n-z)), mod, fif)
    ans %= mod
    if ans < 0:
        ans += mod
    print(ans)