def main():
    k = int(input())
    s = input()
    n = len(s)

    def cmb1(n, r, mod):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    mod = 10**9+7
    N = 2*10**6
    fac = [1]*(N+1)
    finv = [1]*(N+1)
    for i in range(N):
        fac[i+1] = fac[i] * (i+1) % mod
    finv[-1] = pow(fac[-1], mod-2, mod)
    for i in reversed(range(N)):
        finv[i] = finv[i+1] * (i+1) % mod

    def cmb1(n, r, mod):
        if r <0 or r > n:
            return 0
        r = min(r, n-r)
        return fac[n] * finv[r] * finv[n-r] % mod

    def power(a, n, mod):
        bi=str(format(n,"b")) #2進数
        res=1
        for i in range(len(bi)):
            res=(res*res) %mod
            if bi[i]=="1":
                res=(res*a) %mod
        return res

    ans = 0
    for i in range(k+1):
        temp = power(25, i, mod)
        temp *= cmb1(i+n-1, n-1, mod)
        temp %= mod
        temp *= power(26, k-i, mod)
        temp %= mod
        ans += temp
    print(ans%mod)

if __name__ == '__main__':
    main()
