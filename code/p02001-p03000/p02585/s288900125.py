# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


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
def slv(N, K, P, C):
    P = [p-1 for p in P]

    done = set()
    cycles = []
    for i in range(N):
        c = i
        t = []
        while c not in done:
            n = P[c]
            done.add(c)
            t.append(c)
            c = n
        if t:
            cycles.append(t)

    ans = -INF
    for c in cycles:
        cs = sum(C[v] for v in c)
        if cs > 0:
            m = max(0, (K // len(c)) - 1)
            k = K - len(c) * m
            a = cs * m
            ans = max(ans, a)
        else:
            k = min(len(c), K)
            a = 0

        b = a
        for u in c:
            a = b
            for _ in range(k):
                v = P[u]
                a += C[v]
                ans = max(ans, a)
                u = v

    return ans


def main():
    N, K = read_int_n()
    P = read_int_n()
    C = read_int_n()
    print(slv(N, K, P, C))


if __name__ == '__main__':
    main()
