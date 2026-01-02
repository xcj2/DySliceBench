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
def slv(N, UVW):
    g = defaultdict(dict)
    for u, v, w in UVW:
        g[u][v] = w
        g[v][u] = w

    for i in range(1, N+1):
        if len(g[i]) == 1:
            s = i
            break

    C = [-1] * (N+1)
    C[s] = 0
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        for v, w in g[u].items():
            if C[v] == -1:
                q.append(v)
                if w % 2 == 0:
                    C[v] = C[u]
                else:
                    C[v] = C[u] ^ 1

    for c in C[1:]:
        print(c)
    return


def main():
    N = read_int()
    UVW = [read_int_n() for _ in range(N-1)]
    slv(N, UVW)


if __name__ == '__main__':
    main()
