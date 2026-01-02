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
def slv(N, M, LRD):
    # print(LRD)
    g = [[] for _ in range(N)]
    ns = set([])
    for l ,r, d in LRD:
        g[l-1].append((r-1,d))
        g[r-1].append((l-1,-d))
        ns.add(l-1)
        ns.add(r-1)      
    
    G =  [None for _ in range(N)]

    if M == 0:
        return 'Yes'

    ns = {n:n for n in ns}
    while ns:
        # q = [list(ns.keys())[0]]
        for k in ns.keys():
            q = [k]
            break
        ns.pop(q[0])
        # print(q)
        G[q[0]] = 0
        while q:
            n = q.pop()
            for r, d in g[n]:
                if G[r] is None:
                    G[r] = G[n] + d
                    q.append(r)
                    # if r in ns:
                    ns.pop(r)
                else:
                    if G[r] != G[n] + d:
                        return 'No'
                        # pass
    
    return 'Yes'
            



def main():
    N, M = read_int_n()
    LRD = [read_int_n() for _ in range(M)]

    # N = 100000
    # M = 200000
    # LRD = [[random.randint(1, N), random.randint(1, N), random.randint(1, 10000)] for _ in range(M) ]
    print(slv(N, M, LRD))


if __name__ == '__main__':
    main()
