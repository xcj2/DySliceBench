from sys import stdin, setrecursionlimit
from math import factorial

setrecursionlimit(10 ** 9)
INF = 1 << 60


def input():
    return stdin.readline().strip()


def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    COM_MAX = N

    fac, finv, inv = [0] * (COM_MAX + 1), [0] * (COM_MAX + 1), [0] * (COM_MAX + 1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2, COM_MAX + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    def mod_com(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

    ans = 0
    power = M % MOD
    for k in range(N - 1, -1, -1):
        if k <= K:
            ans += mod_com(N - 1, k) * power % MOD
        power = power * (M - 1) % MOD

    print(ans % MOD)

    return


if __name__ == '__main__':
    main()
