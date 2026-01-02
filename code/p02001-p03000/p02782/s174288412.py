def main():
    MOD = 10**9 + 7
    r1, c1, r2, c2 = (int(i) for i in input().split())
    m = r2 + c2 + 3
    fac = [0] * m
    finv = [0] * m
    inv = [0] * m

    def COMBinitialize(m):
        fac[0] = 1
        finv[0] = 1
        if m > 1:
            fac[1] = 1
            finv[1] = 1
            inv[1] = 1
            for i in range(2, m):
                fac[i] = fac[i-1] * i % MOD
                inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
                finv[i] = finv[i - 1] * inv[i] % MOD

    def COMB(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

    COMBinitialize(m)
    ans = 0
    ans += (fac[r2+1+c2+1]*finv[r2+1]*finv[c2+1] - 1) % MOD
    ans -= (fac[r2+1+c1]*finv[r2+1]*finv[c1] - 1) % MOD
    ans -= (fac[r1+c2+1]*finv[r1]*finv[c2+1] - 1) % MOD
    ans += (fac[r1+c1]*finv[r1]*finv[c1] - 1) % MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
