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
import copy

sys.setrecursionlimit(100000)
input = sys.stdin.readline


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
def slv(N, GSB):
    def f(N, gsb):
        dp0 = [0] * (N+1)
        dp1 = [0] * (N+1)
        for i in range(3):
            v = gsb[1][i] - gsb[0][i]
            a = gsb[0][i]
            if v > 0:
                for w in range(N+1):
                    if w >= a:
                        dp1[w] = max(dp0[w], dp1[w-a] + v)
            else:
                dp1 = dp0
            dp0 = dp1
            dp1 = copy.copy(dp0)
        return dp0[N] + N
    tmp = f(N, GSB)
    # print(tmp)
    GSB[0], GSB[1] = GSB[1], GSB[0]
    return f(tmp, GSB)


def main():
    N = read_int()
    GSB = [read_int_n() for _ in range(2)]
    print(slv(N, GSB))


if __name__ == '__main__':
    main()
