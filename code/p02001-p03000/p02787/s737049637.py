#!/usr/bin/env python3
import sys
import collections as cl
import math


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    h, n = MI()
    a = []
    b = []
    for _ in range(n):
        _a, _b = MI()
        a.append(_a)
        b.append(_b)

    max_a = max(a)

    dp = [0] * (h + max_a + 1)

    for i in range(1, h + max_a + 1):
        min_itr = 10**19

        for j in range(n):
            if i - a[j] > 0:
                min_itr = min(min_itr, dp[i - a[j]] + b[j])

            else:
                min_itr = min(min_itr, b[j])

        dp[i] = min_itr

    print(min(dp[h:h+max_a]))


main()
