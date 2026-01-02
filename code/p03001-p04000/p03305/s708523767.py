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


@mt
def slv(n, m, s, t, UVAB):
    g = defaultdict(list)
    for u, v, a, b in UVAB:
        g[u].append((v, (a, b)))
        g[v].append((u, (a, b)))

    def d(s, ck):
        dist = [0 if s == i else sys.maxsize for i in range(n+1)]
        # p = [None for i in range(n+1)]
        q =[]
        heapq.heappush(q, (dist[s], s))
        while q:
            c, u = heapq.heappop(q)
            if dist[u] > c:
                continue
            for v, cost in g[u]:
                alt = dist[u] + cost[ck]
                if dist[v] > alt:
                    dist[v] = alt
                    heapq.heappush(q, (alt, v))
        return dist

    dist0 = d(s, 0)
    dist1 = d(t, 1)

    ans = [sys.maxsize] * (n+1)
    
    for i in range(n-1, -1, -1):
        # print(i)
        ans[i] = min(ans[i+1], dist1[i+1] + dist0[i+1])
    c = 10**15
    return '\n'.join(map(lambda x: str(c-x), ans[:-1]))


def main():
    n, m, s, t = read_int_n()
    UVAB = [read_int_n() for _ in range(m)]

    
    print(slv(n, m, s, t, UVAB))


if __name__ == '__main__':
    main()
