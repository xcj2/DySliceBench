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
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 2**62-1


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


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(S, X, Y):
    m = list(map(lambda x: len(x), S.split('T')))

    X -= m[0]
    ym = m[1::2]
    xm = m[2::2]

    memo = {0}
    for dx in xm:
        nm = set()
        for x in memo:
            nm.add(x+dx)
            nm.add(x-dx)
        memo = nm
    if X not in memo:
        return 'No'

    memo = {0}
    for dy in ym:
        nm = set()
        for y in memo:
            nm.add(y+dy)
            nm.add(y-dy)
        memo = nm
    if Y not in memo:
        return 'No'

    return 'Yes'




def main():
    S = read_str()
    X, Y = read_int_n()
    print(slv(S, X, Y))


if __name__ == '__main__':
    main()
