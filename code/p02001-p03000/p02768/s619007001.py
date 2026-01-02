import math

def modpow(a, n , mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a*a % mod
        n >>= 1
    return res

def calcp(n,j,mod):
    res = 1
    for i in range(n,n-j,-1):
        res = res * i %mod
    return res

def main():
    n,a,b = list(map(int, input().split()))
    MOD = 10**9+7
    NMAX = 2*10**5

    fact = [0 for i in range(NMAX+5)]
    fact[0] = 1
    invfact = [0 for i in range(NMAX+5)]
    invfact[0] = 1

    for i in range(NMAX):
        fact[i+1] = (fact[i]*(i+1))%(MOD)

    invfact[NMAX] = pow(fact[NMAX], MOD-2, MOD)
    for i in range(NMAX-1,0,-1):
        invfact[i] = (invfact[i+1] * (i+1)) % MOD

    ans = modpow(2,n,MOD)-1

    pa = calcp(n,a,MOD)*invfact[a]%MOD
    pb = calcp(n,b,MOD)*invfact[b]%MOD
    ans = ans - pa - pb;
    while ans < 0:
        ans += MOD
    print(ans)

        

main()