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
def slv(N, S):
    E = []
    G = defaultdict(list)
    for i, s in enumerate(S):
        for j, c in enumerate(s[:]):
            if i < j and c == '1':
                E.append((i, j))
                G[i].append(j)
                G[j].append(i)
    
    def f(s):
        e = set(E)
        vs = [set([s])]
        while e:
            vs1 = set()
            for i in vs[-1]:
                for j in G[i]:
                    vs1.add(j)
                    if i > j:
                        u, v = j, i
                    else:
                        u, v = i, j
                    if (u, v) in e:
                        e.remove((u, v))
            vs.append(vs1)
            for i in vs[-1]:
                for j in G[i]:
                    if j in vs[-1]:
                        return -1

        return len(vs)

    ans = -1
    for i in range(N):
        ans = max(ans, f(i))
    return ans


def main():
    N = read_int()
    S = [read_str() for _ in range(N)]
    print(slv(N, S))

if __name__ == '__main__':
    main()
