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
def slv(N, M, A, B, C, P, Q, R):
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort()
    P = P[:N]
    Q = Q[:M]

    S = P + Q
    heapq.heapify(S)
    for r in R:
        if r > S[0]:
            heapq.heappop(S)
            heapq.heappush(S, r)

    return sum(S)


def main():
    N, M, A, B, C = read_int_n()
    P = read_int_n()
    Q = read_int_n()
    R = read_int_n()
    print(slv(N, M, A, B, C, P, Q, R))


if __name__ == '__main__':
    main()
