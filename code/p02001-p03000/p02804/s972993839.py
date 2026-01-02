def main():
    import sys
    input = sys.stdin.buffer.readline
    MOD = 10**9 + 7
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    m = N+5
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
    minS = 0
    maxS = 0
    for i in range(K-1, N):
        maxS += A[i]*COMB(i, K-1)
        maxS %= MOD
    for i in range(N-K+1):
        minS += A[i]*COMB(N-i-1, K-1)
        minS %= MOD
    ans = maxS - minS
    ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
