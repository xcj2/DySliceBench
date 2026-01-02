import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())

    MOD = 10 ** 9 + 7
    fact = [1, 1]  # fact[n] = (n! mod MOD)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod MOD)
    inv = [0, 1]

    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

    def cmb(n, r, p):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * factinv[r] * factinv[n - r] % p

    for i in range(1, K + 1):
        res = cmb(N - K + 1, i, MOD) * cmb(K - 1, i - 1, MOD)
        res %= MOD
        print(res)


if __name__ == '__main__':
    main()
