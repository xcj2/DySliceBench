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
def slv(H, W, A):
    cost = [[-1] * W for _ in range(H)]
    bq = deque()
    for i in range(H):
        for j in range(W):
            if A[i][j] == "#":
                bq.append((i, j))
                cost[i][j] = 0

    while bq:
        i, j = bq.popleft()
        c = cost[i][j]
        if i > 0 and cost[i-1][j] == -1:
            cost[i-1][j] = c + 1
            bq.append((i-1, j))

        if i < H-1 and cost[i+1][j] == -1:
            cost[i+1][j] = c + 1
            bq.append((i+1, j))

        if j > 0 and cost[i][j-1] == -1:
            cost[i][j-1] = c + 1
            bq.append((i, j-1))

        if j < W-1 and cost[i][j+1] == -1:
            cost[i][j+1] = c + 1
            bq.append((i, j+1))

    return max(map(max, cost))


def main():
    H, W = read_int_n()
    A = [read_str() for _ in range(H)]
    print(slv(H, W, A))


if __name__ == '__main__':
    main()
