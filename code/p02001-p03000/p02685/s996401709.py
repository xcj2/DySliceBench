import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M, K = map(int, input().split())

    MOD = 998244353

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

    E = [1]
    for _ in range(N):
        e = E[-1] * (M - 1)
        e %= MOD
        E.append(e)

    res = 0
    for k in range(0, K + 1):
        a = N - 1 - k

        b = cmb(N - 1, a, MOD) % MOD
        b *= M
        b %= MOD
        b *= E[a]
        b %= MOD

        res += b
        res %= MOD

    print(res)


if __name__ == '__main__':
    main()
