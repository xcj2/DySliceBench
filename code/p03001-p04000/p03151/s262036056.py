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
import re
sys.setrecursionlimit(10000)


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
def slv(N, A, B):
    if sum(A) < sum(B):
        return -1

    P = []
    M = []
    for i in range(N):
        d = A[i] - B[i]
        if d > 0:
            P.append(d)
        elif d < 0:
            M.append(d)

    P.sort()
    M.sort()

    c = 0
    ans = 0
    for m in M:
        while -m > c:
            c += P.pop()
            ans += 1
        c += m
        ans += 1

    return ans


def main():
    N = read_int()
    A = read_int_n()
    B = read_int_n()
    print(slv(N, A, B))


if __name__ == '__main__':
    main()
