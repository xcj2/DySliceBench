N,M = map(int,input().split())

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def modpow(a,n,mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

def modinv(a,mod):
    return modpow(a,mod - 2,mod)

def cnk(a,b):
    MOD = 10**9+7
    ret = 1
    for i in range(b):
        ret *= (a-i)
        ret %= MOD
        ret = ret * modinv(i+1,MOD) % MOD
    return ret

lis = factorize(M)
ans = 1
for l in lis:
    ans *= cnk(l[1]+N-1,N-1)
    ans %= 10**9+7

print(ans)
