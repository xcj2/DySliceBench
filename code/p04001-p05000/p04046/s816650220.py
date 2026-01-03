def main():
    H, W, A, B = (int(i) for i in input().split())
    m = H + W + 3
    MOD = 10**9 + 7
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
    for x in range(W-B):
        if x == 0:
            p = COMB(H-A-1 + B+x, B+x)
        else:
            p = COMB(H-A-1 + B+x, B+x) - COMB(H-A-1 + B+x-1, B+x-1)
        q = COMB(A+W-1-B-x, A)
        ans += p*q
        ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
