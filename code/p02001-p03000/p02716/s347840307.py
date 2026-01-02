# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 2**62-1

def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, A):
    m = N // 2
    dp = [defaultdict(lambda: -INF)] * 2
    dp[0][0] = 0
    for i, a in enumerate(A):
        ndp = [defaultdict(lambda: -INF)] * 2
        l = m - ((N-i) // 2)
        ndp[0] = dp[1]
        for k, v in dp[0].items():
            if k+1 >= l:
                ndp[1][k+1] = max(ndp[1][k+1], v+a)
            if k+2 >= l:
                ndp[0][k] = max(ndp[0][k], v)
        dp = ndp
    return max(dp[0][m], dp[1][m])


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))

if __name__ == '__main__':
    main()
