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
def slv(N, A):
    c = Counter(A)
    ks = list(c.keys())
    ks.sort()

    ans = 0
    for k in ks:
        if c[k] % 2 == 1:
            c.pop(k)
            ans += 1
        else:
            c[k] = 2

    ans += len(c)
    if len(c) % 2 == 1:
        ans -= 1

    return ans


def main():
    N = read_int()
    A = read_int_n()

    print(slv(N, A))


if __name__ == '__main__':
    main()
