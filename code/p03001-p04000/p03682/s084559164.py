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
def slv(N, XY):
    g = defaultdict(dict)
    V = [(i, x, y) for i, (x, y) in enumerate(XY)]
    V.sort(key=lambda x: x[1])
    for i in range(1, N):
        v = V[i][0]
        u = V[i-1][0]
        d = min(abs(XY[v][0] - XY[u][0]), abs(XY[v][1] - XY[u][1]))
        g[v][u] = d
        g[u][v] = d

    V.sort(key=lambda x: x[2])
    for i in range(1, N):
        v = V[i][0]
        u = V[i-1][0]
        d = min(abs(XY[v][0] - XY[u][0]), abs(XY[v][1] - XY[u][1]))
        g[v][u] = d
        g[u][v] = d

    return Prim(g)


def main():
    N = read_int()
    XY = [read_int_n() for _ in range(N)]

    print(slv(N, XY))


if __name__ == '__main__':
    main()
