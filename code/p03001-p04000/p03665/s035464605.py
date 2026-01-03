import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    def fast_pow(num, kata, mod):
        if kata == 0:
            return 0

        res = 1
        while kata > 0:
            if kata & 1 == 1:
                res = res * num % mod
            num = num * num % mod

            kata >>= 1
        return res

    def choose(l, r):
        res = 1
        fac = 1
        for j in range(r):
            res *= l - j
            fac *= j + 1
        return res // fac

    n, p = ns()
    a = na()

    cnt = [0, 0]

    for ai in a:
        if ai % 2:
            cnt[1] += 1
        else:
            cnt[0] += 1

    zero_choice = 2 ** cnt[0]
    one_choice = 0
    for i in range(p, cnt[1] + 1, 2):
        one_choice += choose(cnt[1], i)

    print(zero_choice * one_choice)


if __name__ == '__main__':
    main()
