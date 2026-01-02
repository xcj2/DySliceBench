#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    n, q = read_h()
    s, = read_h(typ=str)
    rng = read_v(q, m=2)

    cnts = [0] * (n + 1)
    for i in range(len(s)):
        cnts[i + 1] = cnts[i] + (1 if s[i:i + 2] == 'AC' else 0)

    for l, r in rng:
        print(cnts[r - 1] - cnts[l - 1])


if __name__ == '__main__':
    main()
