MOD = 10**9+7
lim = 200000
inv_t = [-1 for i in range(lim+1)]
factrial = [-1 for i in range(lim+1)]
factrial_inv = [-1 for i in range(lim+1)]


def mod_inv(x, mod=MOD):
    y, u, v, _x = mod, 1, 0, x
    while y:
        t = _x//y
        _x -= t*y
        _x, y = y, _x
        u -= t*v
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u


def mod_pow(a, n, mod=MOD):
    res = 1
    while n:
        if n & 1:
            res = res*a % mod
        a = a*a % mod
        n >>= 1
    return res


def COMinit(max=lim, mod=MOD):
    factrial[0] = factrial_inv[0] = 1
    factrial[1] = factrial_inv[1] = 1
    inv_t[0] = inv_t[1] = 1
    for i in range(2, max):
        factrial[i] = factrial[i-1]*i % mod
        inv_t[i] = mod-inv_t[mod % i]*(mod//i) % mod
        factrial_inv[i] = factrial_inv[i-1]*inv_t[i] % mod


def comb(a, b, mod=MOD):
    if a < b:
        return 0
    if factrial[0] == -1:
        COMinit()
    return (factrial[a]*factrial_inv[b]*factrial_inv[a-b]) % mod


n, k = [int(_) for _ in input().split()]
for i in range(k):
    print(comb(n-k+1, i+1)*comb(k-1, i) % MOD)
