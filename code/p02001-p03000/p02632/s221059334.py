# 解説AC
# 解説放送と
# https://twitter.com/kyopro_friends/status/1274710268262547456?s=20
# で理解
MOD = 10**9 + 7


def main():
    K = int(input())
    S = input()
    N = len(S)
    m = N+K + 5
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
    for i in range(K+1):
        v = COMB(N-1+K-i, N-1)
        v %= MOD
        v *= pow(25, (K-i), MOD)
        v %= MOD
        v *= pow(26, i, MOD)
        v %= MOD
        ans += v
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
