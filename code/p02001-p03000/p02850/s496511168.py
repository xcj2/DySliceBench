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
def slv(N, AB):
    g = defaultdict(list)
    for a, b in AB:
        g[a].append(b)
        g[b].append(a)
        
    s = [(1, -1)]
    done = set([1])
    K = 1
    ans = {}
    while s:
        u, c = s.pop()
        used = set([c])
        c = 1
        for v in g[u]:
            if v in done:
                continue
            while c in used:
                c += 1 
                K = max(K, c)
            used.add(c)
            s.append((v, c))
            i, j = min(u, v), max(u, v)
            ans[(i, j)] = c
            done.add(v)
    print(K)
    for a, b in AB:
        print(ans[(a, b)])
    # return ans


def main():
    N = read_int()
    AB = [read_int_n() for _ in range(N-1)]
    (slv(N, AB))


if __name__ == '__main__':
    main()
