
# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from pprint import pprint
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul

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


def Prim(g):
    V = list(g.keys())
    for v in g.values():
        V.extend(list(v.keys()))
    V = list(set(V))

    used = set([])
    q = []
    heapq.heappush(q, (0, V[0]))

    ret = 0
    while q:
        c, v = heapq.heappop(q)

        if v in used:
            continue
        used.add(v)
        ret += c
        for u in g[v]:
            heapq.heappush(q, (g[v][u], u))
    return ret


@mt
def slv(N, A):
    q = []
    lc = [0]*(N+1)
    for i in range(N):
        heapq.heappush(q, A[i])
        lc[0] += A[i]
    for i in range(N, 2*N):

        a = heapq.heappushpop(q, A[i])
        lc[i-N+1] = lc[i-N] + A[i] - a

    q = []
    rc = [0] * (N+1)
    for i in range(3*N-1, 2*N-1, -1):
        heapq.heappush(q, -A[i])
        rc[N] += A[i]
    for i in range(2*N-1, N-1, -1):
        a = -heapq.heappushpop(q, -A[i])
        rc[i-N] = rc[i-N+1] + A[i] - a

    return max(map(lambda x: x[0]-x[1], zip(lc, rc)))


def main():
    N = read_int()
    A = read_int_n()

    print(slv(N, A))


if __name__ == '__main__':
    main()
