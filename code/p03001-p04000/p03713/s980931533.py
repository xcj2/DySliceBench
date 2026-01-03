
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
from operator import add, mul, sub

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
def slv(H, W):
    if H % 3 == 0 or H % 3 == 0:
        return 0

    L = max(H, W)
    S = min(H, W)

    def f1(L, S):
        if (math.ceil(L/3) - L/3) < (L/3 - math.floor(L/3)):
            SL = math.ceil(L/3)
        else:
            SL = math.floor(L/3)
        A = SL * S

        L -= SL
        if L < S:
            L, S = S, L

        if L % 2 == 0 or S % 2 == 0:
            B = C = (L * S) // 2
        else:
            if (math.ceil(L/2) - L/2) < (L/2 - math.floor(L/2)):
                SL = math.ceil(L/2)
            else:
                SL = math.floor(L/2)
            B = SL * S
            C = (L-SL) * S
        return max([A, B, C]) - min([A, B, C])

    def f2(L, S):
        if (math.ceil(S/3) - S/3) < (S/3 - math.floor(S/3)):
            SL = math.ceil(S/3)
        else:
            SL = math.floor(S/3)
        A = SL * L

        S -= SL
        if L < S:
            L, S = S, L

        if L % 2 == 0 or S % 2 == 0:
            B = C = (L * S) // 2
        else:
            if (math.ceil(L/2) - L/2) < (L/2 - math.floor(L/2)):
                SL = math.ceil(L/2)
            else:
                SL = math.floor(L/2)
            B = SL * S
            C = (L-SL) * S
        return max([A, B, C]) - min([A, B, C])

    return min(f1(H, W), f2(H, W))


def main():
    H, W = read_int_n()

    print(slv(H, W))


if __name__ == '__main__':
    main()
