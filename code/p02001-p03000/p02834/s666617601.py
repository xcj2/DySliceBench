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

    s = [U]
    prev = {}
    prev[U] = -1
    while s:
        u = s.pop()
        for v in g[u]:
            if v in prev:
                continue
            prev[v] = u
            s.append(v)

    p = [V]
    v = V
    while v != U:
        v = prev[v]
        p.append(v)
    p.reverse()
    nu = p[len(p)//2-1]
    ans = len(p)//2-1
    if len(p) % 2 == 1:
        ans += 1

    done = set(p[len(p)//2-1:])

    d = {nu: 0}
    s = [nu]
    while s:
        u = s.pop()
        for v in g[u]:
            if v in done:
                continue
            d[v] = d[u] + 1
            done.add(u)
            s.append(v)

    return ans + max(d.values())





def main():
    N, U, V = read_int_n()
    AB = [read_int_n() for _ in range(N-1)]
    print(slv(N, U, V, AB))


if __name__ == '__main__':
    main()
