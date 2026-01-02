#!/usr/bin/env python3
import collections as cl
import sys


def comb(n, r, mod=10 ** 9 + 7):
    r = min(r, n-r)
    upper = 1

    for i in range(n, n-r, -1):
        upper = (upper * i) % mod

    lower = 1

    for i in range(1, r+1):
        lower = (lower * i) % mod

    lower_inv = pow(lower, mod - 2, mod)

    return (upper * lower_inv) % mod


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, a, b = MI()

    ttl = pow(2, n, 10**9+7) - 1

    a_ttl = comb(n, a)
    b_ttl = comb(n, b)

    print((ttl - a_ttl - b_ttl) % (10**9+7))


main()
