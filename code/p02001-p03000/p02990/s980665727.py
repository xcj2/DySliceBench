import sys

# import re
import math
import collections
# import decimal
# import bisect
# import itertools
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

    # MODのCombination nがでかくても関係なくrに依存　r<10**6なら回せる
    MOD = 10 ** 9 + 7

    def choose(n, r):
        res = 1
        fac = 1
        for i in range(r):
            res *= n - i
            res %= MOD
            fac *= i + 1
            fac %= MOD
        return res * fast_pow(fac, MOD - 2, MOD) % MOD

    n, k = ns()

    for i in range(1, k + 1):
        blue_pair = choose(k - i + (i - 1), i - 1)
        red_pair = choose((n - k) + 1, i)
        print(blue_pair * red_pair % MOD)


if __name__ == '__main__':
    main()
