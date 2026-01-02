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


def f(n):
    v = 0
    for i in range(60):
        if 1 << i & n:
            v += (-2)**i
    return v

# @mt
def slv(N):
    v = N
    for i in range(60):
        b = 1 if 1 << i & v > 0 else 0
        if b and i % 2 != 0:
            v += 1 << (i+1)

    return v


def main():
    N = read_int()
    print(bin(slv(N))[2:])



if __name__ == '__main__':
    main()
