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


class FenwicTree:
    def __init__(self, n):
        self.__data = [0] * n
        self.__n = n

    def add(self, i, x):
        i += 1
        while i <= self.__n:
            self.__data[i-1] += x
            i += i & -i

    def sum(self, l, r):
        return self.__sum(r) - self.__sum(l)

    def __sum(self, r):
        s = 0
        while r > 0:
            s += self.__data[r-1]
            r -= r & -r

        return s


@mt
def slv(N, A, Q):
    ft = FenwicTree(N)
    for i, a in enumerate(A):
        ft.add(i, a)

    ans = []
    for q in Q:
        if q[0] == 0:
            _, p, x = q
            ft.add(p, x)
        else:
            _, l, r = q
            ans.append(ft.sum(l, r))

    return ans


def main():
    N, Q = read_int_n()
    A = read_int_n()
    Q = [read_int_n() for _ in range(Q)]
    print(*slv(N, A, Q), sep='\n')



if __name__ == '__main__':
    main()
