# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
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
    return input()


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


def warshall_floyd(g):
    d = defaultdict(dict)
    V = list(g.keys())
    for v in g.values():
        V.extend(list(v))
    V = set(V)
    for i in V:
        for j in V:
            if i in g and j in g[i]:
                d[i][j] = g[i][j]
            else:
                d[i][j] = sys.maxsize
    for k in g:
        for i in g:
            for j in g:
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d


@mt
def slv(H, W, C, A):
    g = defaultdict(dict)
    for i in range(10):
        for j in range(10):
            g[i][j] = C[i][j]

    d = warshall_floyd(g)

    a = Counter()
    for r in A:
        for n in r:
            a[n] += 1

    ans = 0
    for k in a:
        if k != -1:
            ans += d[k][1] * a[k]
    return ans


def main():
    H, W = read_int_n()
    C = [read_int_n() for _ in range(10)]
    A = [read_int_n() for _ in range(H)]
    print(slv(H, W, C, A))


if __name__ == '__main__':
    main()
