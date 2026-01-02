def main():
    X, Y = (int(i) for i in input().split())
    fac = [0] * max(X, Y)
    finv = [0] * max(X, Y)
    inv = [0] * max(X, Y)
    MOD = (10**9) + 7

    def COMinit(m):
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

    def COM(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

    COMinit(max(X, Y))
    if (X+Y) % 3 != 0:
        return print(0)
    n = (2*Y - X) // 3
    m = (2*X - Y) // 3
    print(COM(n+m, m))


if __name__ == '__main__':
    main()
