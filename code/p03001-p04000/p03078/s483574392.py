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
def slv(X, Y, Z, K, A, B, C):
    q = []

    for a in A:
        for b in B:
            if len(q) < K:
                heapq.heappush(q, a+b)
            else:
                heapq.heappushpop(q, a+b)

    qq = []
    for c in C:
        for d in q:
            if len(qq) < K:
                heapq.heappush(qq, d+c)
            else:
                heapq.heappushpop(qq, d+c)

    qq.sort(reverse=True)
    return qq

def main():
    X, Y, Z, K = read_int_n()
    A = read_int_n()
    B = read_int_n()
    C = read_int_n()
    print(*slv(X, Y, Z, K, A, B, C), sep='\n')


if __name__ == '__main__':
    main()
