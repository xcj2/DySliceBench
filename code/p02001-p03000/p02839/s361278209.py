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
def slv(H, W, A, B):
    M = [[abs(a-b) for a, b in zip(ar, br)] for ar, br in zip(A, B)]
    S = W*H*80
    dp = [[0 for _ in range(W)] for __ in range(H)]
    dp[0][0] = 1 << (S-M[0][0]) | 1 << (S+M[0][0])
    for i in range(H):
        for j in range(W):
            for k, l in [(-1, 0), (0, -1)]:
                D = M[i][j]
                dp[i][j] |= dp[i+k][j+l] << D
                dp[i][j] |= dp[i+k][j+l] >> D

    ans = None
    cand = dp[H-1][W-1]
    for i in range(H*W*80):
        if cand & (1 << (S+i)) != 0:
            ans = i
            break
    assert ans is not None
    return ans


def main():
    H, W = read_int_n()
    A = [read_int_n() for _ in range(H)]
    B = [read_int_n() for _ in range(H)]
    print(slv(H, W, A, B))

    # H = 80
    # W = 80

    # # A = [[random.randint(0, 1000) for __ in range(W)] for _ in range(H)]
    # # B = [[random.randint(0, 1000) for __ in range(W)] for _ in range(H)]
    # A = [[0 for __ in range(W)] for _ in range(H)]
    # B = [[random.randint(0, 80) for __ in range(W)] for _ in range(H)]
    # print(slv(H, W, A, B))


if __name__ == '__main__':
    main()
