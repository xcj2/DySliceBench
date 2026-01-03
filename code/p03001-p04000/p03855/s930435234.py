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
def slv(N, K, L, PQ, RS):
    ans = 0
    gr = defaultdict(list)
    for p, q in PQ:
        gr[p].append(q)
        gr[q].append(p)

    gt = defaultdict(list)
    for r, s in RS:
        gt[r].append(s)
        gt[s].append(r)

    ccr = {}
    unused = set(gr.keys())
    while unused:
        q = [unused.pop()]
        con = set([])
        while q:
            v = q.pop()
            con.add(v)
            for u in gr[v]:
                if u in unused:
                    q.append(u)
                    unused.remove(u)
        for v in con:
            ccr[v] = con

    cct = {}
    unused = set(gt.keys())
    while unused:
        q = [unused.pop()]
        con = set([])
        while q:
            v = q.pop()
            con.add(v)
            for u in gt[v]:
                if u in unused:
                    q.append(u)
                    unused.remove(u)
        for v in con:
            cct[v] = con

    cache = {}

    def cc(t, r):
        k = (id(t), id(r))
        if k not in cache:
            cache[k] = len(t & r)
        return cache[k]

    ans = []
    for i in range(1, N+1):
        if i in cct and i in ccr:
            a = cc(cct[i], ccr[i])
        else:
            a = 1
        ans.append(a)
    return " ".join(map(str, ans))


def main():
    N, K, L = read_int_n()
    PQ = [read_int_n() for _ in range(K)]
    RS = [read_int_n() for _ in range(L)]

    print(slv(N, K, L, PQ, RS))


if __name__ == '__main__':
    main()
