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
INF = 2**62-1

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


def is_biparty(g):
    u = list(g.keys())[0]
    s = [u]
    c = {}
    c[u] = True
    while s:
        u = s.pop()
        for v in g[u]:
            if v not in c:
                c[v] = not c[u]
                s.append(v)
            else:
                if c[v] == c[u]:
                    return False, None

    return True, c

@mt
def slv(N, M, AB):
    g = defaultdict(set)
    for a, b in AB:
        g[a].add(b)
        g[b].add(a)

    b, c = is_biparty(g)
    if b:
        d = Counter(c.values())
        return d[True] * d[False] - M
    else:
        return N * (N-1) // 2 - M


def main():
    N, M = read_int_n()
    AB = [read_int_n() for _ in range(M)]
    print(slv(N, M, AB))


if __name__ == '__main__':
    main()
