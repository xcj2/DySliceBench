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
def slv(N, M, L):
    l2p = defaultdict(set)
    p2l = defaultdict(set)
    for i, l in enumerate(L):
        p2l[i+1] = set(l)
        for j in l:
            l2p[j].add(i+1)
    
    
    q = [1]
    p_done = set(q)
    l_done = set()
    while q:
        p = q.pop()
        for l in p2l[p]:
            if l in l_done:
                continue
            l_done.add(l)
            for p2 in l2p[l]:
                if p2 in p_done:
                    continue
                p_done.add(p2)
                q.append(p2)
    return 'YES' if set(range(1, N+1)) == p_done else 'NO'



def main():
    N, M = read_int_n()
    L = [read_int_n()[1:] for _ in range(N)]
    print(slv(N, M, L))


if __name__ == '__main__':
    main()
