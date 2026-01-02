# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter


import sys
sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, K, LR):
    M = 998244353
    memo = [0] *(N+2)
    memo[1] = 1
    memo[1+1] = -1
    for i in range(1, N+1):
        memo[i] += memo[i-1]
        memo[i] %= M
        for l, r in LR:
            ll = min(N+1, i+l)
            rr = min(N+1, i+r+1)
            memo[ll] += memo[i]
            memo[ll] %= M
            memo[rr] -= memo[i]
            memo[rr] %= M

    return memo[N]


def main():
    N, K = read_int_n()
    LR = [read_int_n() for _ in range(K)]
    print(slv(N, K, LR))


if __name__ == '__main__':
    main()
