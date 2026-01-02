#!/usr/bin/python3

import os
import sys


def main():
    X, Y = read_ints()
    print(solve(X, Y))


MOD = 10 ** 9 + 7


def mpow(a, n):
    p = a
    v = 1
    while n > 0:
        if n & 1:
            v *= p
            v %= MOD
        n >>= 1
        p *= p
        p %= MOD
    return v


def solve(X, Y):
    s = X + Y
    if s % 3 != 0:
        return 0
    s //= 3

    a = 2 * s - X
    b = 2 * s - Y
    if a < 0 or b < 0:
        return 0

    c = a + b

    facts = [0] * (c + 1)
    facts[0] = 1
    for i in range(1, c + 1):
        facts[i] = (facts[i - 1] * i) % MOD

    return (facts[c] * mpow(facts[a], MOD - 2) * mpow(facts[b], MOD - 2)) % MOD


###############################################################################

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()
