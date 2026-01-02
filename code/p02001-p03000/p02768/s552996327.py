n, a, b = map(int, input().strip().split())
MOD=10**9+7

if n==2:
    print(0)
    exit()

def modpow(x, n, m):
    if n == 0:
        return 1
    res = modpow(x*x%m, n//2, m)
    if n%2 == 1:
        res = res*x%m
    return res

# a*a**(p-2) mod p (Fermat's little theorem)
def modInv(x,m):
    return modpow(x,m-2,m)

def nCr(n,r):
    if r > n-r:
        r=n-r
    denom=1
    numer=1
    for i in range(r):
        denom=(n-i)*denom%MOD
        numer=(i+1)*numer%MOD
    return modInv(numer, MOD)*denom%MOD

ans=modpow(2,n,MOD)-1-nCr(n,a)-nCr(n,b)
print(ans%MOD)