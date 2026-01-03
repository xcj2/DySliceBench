
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


def BellmanFord(g, s):
    V = list(g.keys())
    for v in g.values():
        V.extend(list(v.keys()))
    V = set(V)

    dist = defaultdict(lambda: sys.maxsize)
    pred = defaultdict(lambda: -1)

    dist[s] = 0

    N = len(V)
    for i in range(N+1):
        for u in g:
            for v in g[u]:
                if dist[v] > dist[u] + g[u][v]:
                    if i == N:
                        return 'inf'
                    dist[v] = dist[u] + g[u][v]
                    pred[v] = u
    return dist


@mt
def slv(N, M, ABC):
    g = defaultdict(dict)
    g_ = defaultdict(dict)
    for a, b, c in ABC:
        g_[b][a] = c

    reachable = [N]
    q = [N]
    while q:
        v = q.pop()
        for u in g_[v]:
            if u not in reachable:
                reachable.append(u)
                q.append(u)
    reachable = set(reachable)
    for a, b, c in ABC:
        if a in reachable and b in reachable:
            g[a][b] = -c

    dist = BellmanFord(g, 1)
    if dist == 'inf':
        return 'inf'
    return -1*dist[N]


def main():
    N, M = read_int_n()
    ABC = [read_int_n() for _ in range(M)]

    print(slv(N, M, ABC))


if __name__ == '__main__':
    main()
