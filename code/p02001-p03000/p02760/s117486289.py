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
def slv(A, N, B):
    C = [[False] * 3 for _ in range(3)]
    D = {}
    for i, r in enumerate(A):
        for j, c in enumerate(r):
            D[c] = (i, j)

    for b in B:
        if b in D:
            i, j = D[b]
            C[i][j] = True

    for i in range(3):
        t = True
        for j in range(3):
            t = t and C[i][j]
        if t:
            return 'Yes'

    for i in range(3):
        t = True
        for j in range(3):
            t = t and C[j][i]
        if t:
            return 'Yes'

    t = True
    for i in range(3):
        t = t and C[i][i]
    if t:
            return 'Yes'

    t = True
    for i in range(3):
        t = t and C[2-i][i]
    if t:
            return 'Yes'
    return 'No'


def main():
    A = [read_int_n() for _ in range(3)]
    N = read_int()
    B = [read_int() for _ in range(N)]

    print(slv(A, N, B))


if __name__ == '__main__':
    main()
