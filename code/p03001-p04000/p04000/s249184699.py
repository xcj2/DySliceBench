
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
def slv(H, W, N, AB):
    c = Counter()

    ij = list(product([-1, 0, 1], repeat=2))
    for a, b in AB:
        for i, j in ij:
            c[(a+i, b+j)] += 1

    ans = Counter()
    for (i, j), v in c.items():
        if 2 <= i < H and 2 <= j < W:
            ans[v] += 1

    ans[0] = (H-2) * (W-2) - sum(ans.values())
    for i in range(10):
        print(ans[i])


def main():
    H, W, N = read_int_n()
    AB = [read_int_n() for _ in range(N)]

    slv(H, W, N, AB)


if __name__ == '__main__':
    main()
