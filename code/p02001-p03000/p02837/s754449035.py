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
def slv(N, A):
    ans = 0
    M = [[None] * (N) for _ in range(N)]

    for k, v in A.items():
        for x, y in v:
            M[k-1][x-1] = y

    for i in range(N, 0, -1):
        for m in combinations(range(N), r=i):
            sm = set(m)
            f = True
            for j in m:
                for k, v in enumerate(M[j]):
                    if v == 1 and k not in sm:
                        f = False
                        break
                    elif v == 0 and k in sm:
                        f = False
                        break
                if not f:
                    break

            if f:
                return i
    return 0


def main():
    N = read_int()
    A = {}
    for i in range(1, N+1):
        n = read_int()
        XY = [read_int_n() for _ in range(n)]
        A[i] = XY
    print(slv(N, A))


if __name__ == '__main__':
    main()
