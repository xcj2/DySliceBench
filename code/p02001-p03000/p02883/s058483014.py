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


class Bisect:
    def __init__(self, func):
        self.__func = func

    def bisect_left(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if self.__func(mid) < x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def bisect_right(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if x < self.__func(mid):
                hi = mid
            else:
                lo = mid+1
        return lo

@mt
def slv(N, K, A, F):
    A.sort(reverse=True)
    F.sort()

    def possible(c):
        k = K
        for a, f in zip(A, F):
            d = c//f
            if d - a < 0:
                k += d - a
        if k >= 0:
            return 1
        return 0
    
    b = Bisect(possible)
    return b.bisect_left(1, 0, 10**18)


def main():
    N, K = read_int_n()
    A = read_int_n()
    F = read_int_n()
    print(slv(N, K, A, F))


if __name__ == '__main__':
    main()
