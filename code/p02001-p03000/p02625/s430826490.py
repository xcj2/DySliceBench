# 解説放送見てAC
# 包除原理の演習が足りてないのを感じた
MOD = 10**9 + 7
m = 5 * 10**5 + 500
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


def PERM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[n - k] % MOD) % MOD


COMBinitialize(m)


def main():
    N, M = (int(i) for i in input().split())
    if N == M == 1:
        return print(0)
    ans = 0
    for k in range(N+1):
        ans += PERM(M-k, N-k) * COMB(N, k) * (-1)**(k % 2)
        ans %= MOD
    print(ans * PERM(M, N) % MOD)


if __name__ == '__main__':
    main()
