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
    return tuple(map(int, input().split()))


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
def slv(N, XY):
    c = defaultdict(list)
    for i in range(N):
        x, y = XY[i]
        for j in range(N):
            if i == j:
                continue
            a, b = XY[j]
            c[(x-a, y-b)].append((i, j))

    ans = 0
    for _, v in c.items():
        l = set()
        r = set()

        for x, y in v:
            l.add(x)
            r.add(y)

        g = (len(l) - len(l & r))
        ans = max(ans, len(l | r) - g)
        # print(v, len(l | r), g, l & r)
    return N - ans


def main():
    N = read_int()
    XY = [read_int_n() for _ in range(N)]
    print(slv(N, XY))


if __name__ == '__main__':
    main()
