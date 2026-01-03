
# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from pprint import pprint
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
def slv(N, W, WV):
    items = defaultdict(list)
    for w, v in WV:
        items[w].append(v)

    for w in items:
        items[w].sort(reverse=True)

    for i in range(4-len(items)):
        items[-i] = []
    ws = list(items.keys())

    @lru_cache(maxsize=None)
    def f(rw, i, j, k, l):
        ret = 0
        if ws[0] <= rw and i < len(items[ws[0]]):
            ret = max(ret, f(rw - ws[0], i+1, j, k, l) + items[ws[0]][i])
        if ws[1] <= rw and j < len(items[ws[1]]):
            ret = max(ret, f(rw - ws[1], i, j+1, k, l) + items[ws[1]][j])
        if ws[2] <= rw and k < len(items[ws[2]]):
            ret = max(ret, f(rw - ws[2], i, j, k+1, l) + items[ws[2]][k])
        if ws[3] <= rw and l < len(items[ws[3]]):
            ret = max(ret, f(rw - ws[3], i, j, k, l+1) + items[ws[3]][l])

        return ret

    return f(W, 0, 0, 0, 0)


def main():
    N, W = read_int_n()
    WV = [read_int_n() for _ in range(N)]

    print(slv(N, W, WV))


if __name__ == '__main__':
    main()
