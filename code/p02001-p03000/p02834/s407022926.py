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

INF = 2**62-1


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
def slv(N, U, V, AB):
    g = defaultdict(list)
    for a, b in AB:
        g[a].append(b)
        g[b].append(a)

    def dfs(u):
        s = [u]
        d = {u: 0}
        while s:
            u = s.pop()
            for v in g[u]:
                if v in d:
                    continue
                d[v] = d[u] + 1
                s.append(v)
        return d

    du = dfs(U)
    dv = dfs(V)

    ans = 0
    for v in sorted(du.keys()):
        if du[v] < dv[v]:
            ans = max(ans, dv[v] - 1)

    return ans


def main():
    N, U, V = read_int_n()
    AB = [read_int_n() for _ in range(N-1)]
    print(slv(N, U, V, AB))


if __name__ == '__main__':
    main()
