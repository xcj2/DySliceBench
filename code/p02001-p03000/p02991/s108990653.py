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
input = sys.stdin.readline


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
def slv(N, M, UV, S, T):
    G = defaultdict(list)
    for u, v in UV:
        G[u-1].append(v-1)
    
    S -= 1
    T -= 1
    # print(G)
    d = [defaultdict(lambda: sys.maxsize) for _ in range(N)]
    q = deque([(S, 0, 0)])
    while q:
        u, md, cd = q.popleft()
        if md not in d[u]:
            d[u][md] = min(d[u][md], cd)
            nd = (md+1) % 3
            for v in G[u]:
                q.append((v, nd, cd+1))

    if 0 in d[T]:
        return math.ceil(d[T][0] / 3)
    return -1


def main():
    N, M = read_int_n()
    UV = [read_int_n() for _ in range(M)]
    S, T = read_int_n()
    print(slv(N, M, UV, S, T))


if __name__ == '__main__':
    main()
