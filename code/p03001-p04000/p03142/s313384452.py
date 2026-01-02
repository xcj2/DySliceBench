# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, M, UV):
    g = defaultdict(list)
    fin = Counter()
    for u, v in UV:
        g[u].append(v)
        fin[v] += 1

    r = -1
    for v in range(1, N+1):
        n = fin[v]
        if n == 0:
            r = v
            break

    a = defaultdict(lambda: None)
    q = deque([r])
    a[r] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            fin[v] -= 1
            if fin[v] == 0:
                a[v] = u
                q.append(v)

    ans = [a[i] for i in range(1, N+1)]
    return ans


def main():
    N, M = read_int_n()
    UV = [read_int_n() for _ in range(N-1+M)]
    print(*slv(N, M, UV), sep='\n')


if __name__ == '__main__':
    main()
