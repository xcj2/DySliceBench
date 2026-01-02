MOD = 10**9 + 7


m = 5000
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
            fac[i] = fac[i - 1] * i % MOD
            inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD


def COMB(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


COMBinitialize(m)


def main():
    S = int(input())
    if S < 3:
        print(0)
        return
    ans = 0
    for i in range(1, S // 3 + 1):
        r = S - i * 3
        ans += COMB(r + i - 1, i - 1)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
