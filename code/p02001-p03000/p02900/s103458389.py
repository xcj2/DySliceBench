#!/usr/bin/python3

import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


def main():
    A, B = [int(e) for e in inp().split()]

    G = gcd(A, B)

    ans = 1
    v = G
    p = 2
    while p * p <= v:
        if v % p == 0:
            ans += 1
            v //= p
            while v % p == 0:
                v //= p
        p += 1

    if v > 1:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
