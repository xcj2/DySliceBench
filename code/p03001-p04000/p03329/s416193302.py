# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product

sys.setrecursionlimit(50000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


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


@lru_cache(maxsize=None)
def r(N):
    if N == 0:
        return 0

    c = 1
    while True:
        if c * 9 <= N:
            c *= 9
        else:
            break
    b = 1
    while True:
        if b * 6 <= N:
            b *= 6
        else:
            break
    if c >= 9:
        ac = r(N - c) + 1
    else:
        ac = sys.maxsize

    if b >= 6:
        ab = r(N - b) + 1
    else:
        ab = sys.maxsize

    return min(N, ab, ac)


@mt
def slv(N):
    return r(N)


def main():

    N = read_int()
    print(slv(N))


if __name__ == '__main__':
    main()
