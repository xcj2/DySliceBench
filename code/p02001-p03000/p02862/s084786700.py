# -*- coding: utf-8 -*-
"""
D - Knight
https://atcoder.jp/contests/abc145/tasks/abc145_d

"""
import sys


def modinv(a, m):
    b, u, v = m, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    return u if u >= 0 else u + m


def solve(X, Y):
    MOD = 10**9 + 7
    if (X + Y) % 3:
        return 0
    n = (X - 2 * Y) / -3.0
    m = (Y - 2 * X) / -3.0
    if not n.is_integer() or not m.is_integer() or n < 0 or m < 0:
        return 0
    n, m = int(n), int(m)
    x1 = 1
    for i in range(2, n + m + 1):
        x1 = (x1 * i) % MOD
    x2 = 1
    for i in range(2, n+1):
        x2 = (x2 * i) % MOD
    for i in range(2, m+1):
        x2 = (x2 * i) % MOD
    ans = (x1 * modinv(x2, MOD)) % MOD
    return ans


def main(args):
    X, Y = map(int, input().split())
    ans = solve(X, Y)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
