def main():
    n, k = (int(i) for i in input().split())
    MOD = 10**9 + 7
    m = 2*n + 5
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
    if k >= n - 1:
        print(COMB(2*n-1, n))
    else:
        k = min(k, n-1)  # ここなに？？？？？
        ans = 0
        for m in range(k+1):
            ans += COMB(n, m) * COMB(n-1, n-m-1)
            ans %= MOD
        print(ans % MOD)


if __name__ == '__main__':
    main()
