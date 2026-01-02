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

sys.setrecursionlimit(1000000)
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
def slv(N, K, C, S):
    def f(S):
        r = 0
        w = []
        c = 0
        for s in S:
            if r == 0 and s == 'o':
                w.append(1)
                r = C
                c += 1
            else:
                w.append(0)
                r = max(0, r-1)

        return w
    lw = f(S)
    rw = list(reversed(f(reversed(S))))
    if sum(lw) != K:
        return
    for i, (l, r) in enumerate(zip(lw, rw)):
        if l == r == 1:
            print(i+1)


def main():
    N, K, C = read_int_n()
    S = read_str()
    (slv(N, K, C, S))


if __name__ == '__main__':
    main()
