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
def slv(N, AB):
    g = defaultdict(dict)
    for a, b in AB:
        g[a][b] = 1
        g[b][a] = 1

    f = 1
    s = N

    def df(v):
        d = {v: 0}
        q = [(v, 0)]
        while q:
            v, c = q.pop()
            for u in g[v]:
                if u not in d:
                    d[u] = c + 1
                    q.append((u, c+1))
        return d

    sd = df(s)
    fd = df(f)

    # print(fd)
    # print(sd)

    fc = 0
    sc = 0
    for i in range(2, N):
        if i == s or i == f:
            continue

        if sd[i] >= fd[i]:
            fc += 1
        elif sd[i] < fd[i]:
            sc += 1

    return 'Fennec' if fc > sc else 'Snuke'


def main():
    N = read_int()
    # N, M = read_int_n()
    AB = [read_int_n() for _ in range(N-1)]
    print(slv(N, AB))


if __name__ == '__main__':
    main()
