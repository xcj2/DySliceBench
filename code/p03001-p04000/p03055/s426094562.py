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
    g = defaultdict(set)

    for a, b in AB:
        g[a].add(b)
        g[b].add(a)

    def dfs(s):
        stack = [s]
        done = {s: 0}

        while stack:
            u = stack.pop()
            for v in g[u]:
                if v not in done:
                    done[v] = done[u] + 1
                    stack.append(v)
        l = (-0, 0)
        for k, v in done.items():
            if l[1] < v:
                l = (k, v)
        return l

    v, _ = dfs(1)
    _, l = dfs(v)
    return 'First' if l % 3 != 1 else 'Second'


def main():
    N = read_int()
    AB = [read_int_n() for _ in range(N-1)]
    print(slv(N, AB))


if __name__ == '__main__':
    main()
