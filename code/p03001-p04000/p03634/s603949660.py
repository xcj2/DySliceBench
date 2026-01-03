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


@mt
def slv(N, ABC, Q, K, XY):
    kd = [0] * (N+1)
    kd[K] = 0
    g = defaultdict(dict)
    for a, b, c in ABC:
        g[a][b] = c
        g[b][a] = c

    q = [K]
    while q:
        n = q.pop()
        for m, c in g[n].items():
            if m != K and kd[m] == 0:
                kd[m] = kd[n] + c
                q.append(m)

    for x, y in XY:
        print(kd[x] + kd[y])


def main():
    N = read_int()
    ABC = [read_int_n() for _ in range(N-1)]
    Q, K = read_int_n()
    XY = [read_int_n() for _ in range(Q)]

    slv(N, ABC, Q, K, XY)


if __name__ == '__main__':
    main()
