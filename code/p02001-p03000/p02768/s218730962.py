def modinv(a, mod):
    b = mod
    u = 1
    v = 0
    while(b):
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u

    u %= mod
    return u


def modpow(a, n, mod):
    res = 1
    while(n > 0):
        if (n & 1):
            res = res * a % mod

        a = a * a % mod
        n >>= 1
    
    return res


def modcmb(n, r, mod):
    X = 1
    for i in range(n-r+1, n+1):
        X = X * i % mod

    Y = 1
    for i in range(1, r+1):
        Y = Y * i % mod
        
    res = X * modinv(Y, mod) % mod
    return res


n, a, b = map(int, input().split())
mod = 10**9 + 7

print((modpow(2, n, mod) - 1 - modcmb(n, a, mod) - modcmb(n, b, mod)) % mod)