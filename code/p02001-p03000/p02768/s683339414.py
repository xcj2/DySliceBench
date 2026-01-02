mod = 10**9+7
n, a, b = map(int,input().split())
N = max(a,b)
fact = [None for i in range(N+1)]
fact[0] = 1
for i in range(1, N+1):
    fact[i] = (fact[i-1]*i) % mod
finv = [None for i in range(N+1)]
def inv(x):
    ret = 1
    k = mod - 2
    y = x
    while k:
        if (k & 1):
            ret = (ret * y) % mod
        y = (y * y) % mod
        k //= 2
    return ret
finv[N] = inv(fact[N])
for i in range(N, 0, -1):
    finv[i-1] = (finv[i]*i) % mod
def binpow(x, n, mod=None):
    ret = 1
    while n > 0:
        if n % 2 == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n >>= 1
    return ret
def comb(n,k):
    tmp = 1
    for i in range(k):
        tmp = (tmp*(n-i)) % mod
    return (tmp * finv[k]) % mod
print((binpow(2,n,mod=mod)-1-comb(n,a)-comb(n,b))%mod)