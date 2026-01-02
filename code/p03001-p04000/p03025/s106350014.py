def main():
    mod = 10**9+7
    fact = [1]*200001
    for i in range(1, 200001):
        fact[i] = fact[i-1]*i % mod

    def inv_n(n, mod=10**9+7): return pow(n, mod-2, mod)
    def nCr(n, r, mod=10**9 +
            7): return inv_n(fact[n-r]*fact[r] % mod, mod)*fact[n] % mod
    n, a, b, c = map(int, input().split())
    pan = pow(a, n, mod)
    pbn = pow(b, n, mod)
    ivab = 100*inv_n(a+b) % mod
    ans = 0
    for i in range(n, 2*n):
        ans = (ans + i*ivab*nCr(i-1, n-1)*(pan*pow(b, i-n, mod) +
                                           pow(a, i-n, mod)*pbn)*inv_n(pow(a+b, i, mod))) % mod
    print(ans)


main()
