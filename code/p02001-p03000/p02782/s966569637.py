def main():
    r1, c1, r2, c2 = (int(i) for i in input().split())
    m = r2 + c2 + 3
    fac = [0] * m
    finv = [0] * m
    inv = [0] * m
    MOD = 10**9 + 7

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
    ans = COMB(r2+c2+2, r2+1)
    ans -= COMB(r1+c2+1, r1) + COMB(r2+c1+1, c1)
    ans %= MOD
    ans += COMB(r1+c1, r1)
    print(ans % MOD)


if __name__ == '__main__':
    main()
