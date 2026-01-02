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


@mt
def slv(N, u, v, AB):
    ans = 0
    g = defaultdict(set)
    for a, b in AB:
        g[a].add(b)
        g[b].add(a)


    def f(start):
        s = [(start, 0)]
        d = {}
        d[start] = 0
        while s:
            c, l = s.pop()
            for n in g[c]:
                if n not in d:
                    s.append((n, l+1))
                    d[n] = l+1
        return d

    vd = f(v)
    t = u
    a = v
    s = [(t, 0)]
    d = {}
    d[t] = 0
    while s:
        u, l = s.pop()
        for v in g[u]:
            if v not in d and l + 1 < vd[v]:
                s.append((v, l+1))
                tmp = vd[v] - (l+1)
                tmp = (tmp//2) * 2
                d[v] = tmp + (l+1)

    d[t] = (vd[t] // 2) * 2
    dest = (0, -1)
    for k, v in d.items():
        dest = max(dest, (v, k))

    ans = dest[0]
    # error_print(dest)
    # error_print(d)
    # error_print(vd)
    if vd[dest[1]] == dest[0]:
        ans -= 1
    return ans


def main():
    N, u, v = read_int_n()
    AB = [read_int_n() for _ in range(N-1)]
    print(slv(N, u, v, AB))


if __name__ == '__main__':
    main()
