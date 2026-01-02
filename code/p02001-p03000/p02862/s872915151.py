import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    X, Y = map(int, input().split())

    if (2 * X - Y) % 3 != 0 or (2 * Y - X) % 3 != 0:
        return print(0)

    a = (2 * X - Y) // 3
    b = (2 * Y - X) // 3

    MOD = 10 ** 9 + 7  # 法
    N = a + b  # N!までモジュラ逆数を計算する O(N)
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

    n = a + b  # 総数
    r = min(a, b)  # 選ぶ数
    # nCr = n! * r!^-1 * (n-r)!^-1
    print(cmb(n, r, MOD))


if __name__ == '__main__':
    main()
