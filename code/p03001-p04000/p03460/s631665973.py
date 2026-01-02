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
def slv(N, K, XYC):
    K2 = 2*K
    ans = [[0] * (K2+K2) for _j in range(K2+K2)]
    XY = list(
        map(lambda x:
            (x[0] % K2, (x[1] if x[2] == 'W' else x[1] + K) % K2), XYC
            )
    )

    for x, y in XY:
        ans[x][y] += 1
        ans[x+K][y] -= 1
        ans[x][y+K] -= 1
        ans[x+K][y+K] += 1

        ans[x+K][y+K] += 1
        ans[x+2*K][y+K] -= 1
        ans[x+K][y+2*K] -= 1
        ans[x+2*K][y+2*K] += 1

    for i in range(K2+K2):
        for j in range(1, K2+K2):
            ans[i][j] += ans[i][j-1]
    for i in range(1, K2+K2):
        for j in range(K2+K2):
            ans[i][j] += ans[i-1][j]

    ans_ = [[0] * K2 for _j in range(K2)]
    for i in range(K2+K2):
        for j in range(K2+K2):
            ans_[i % K2][j % K2] += ans[i][j]

    return max(max(r) for r in ans_)


def main():
    N, K = read_int_n()
    XYC = [read_str_n() for _ in range(N)]
    XYC = list(map(lambda x: (int(x[0]), int(x[1]), x[2]), XYC))
    print(slv(N, K, XYC))


if __name__ == '__main__':
    main()
