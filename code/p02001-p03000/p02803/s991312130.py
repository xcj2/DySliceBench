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


def warshall_floyd(g, N):
    d = g
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d


@mt
def slv(H, W, S):
    ans = 0
    g = [[INF] *(H*W) for _ in range(H*W)]
    def idx(i, j):
        return i*W + j
    for i in range(H):
        for j in range(W):
            if S[i][j] != '.':
                continue
            if i > 0 and S[i-1][j] == '.':
                g[idx(i, j)][idx(i-1, j)] = 1

            if i < H-1 and S[i+1][j] == '.':
                g[idx(i, j)][idx(i+1, j)] = 1

            if j > 0 and S[i][j-1] == '.':
                g[idx(i, j)][idx(i, j-1)] = 1

            if j < W-1 and S[i][j+1] == '.':
                g[idx(i, j)][idx(i, j+1)] = 1

    d = warshall_floyd(g, W*H)
    ans = 0
    for i, r in enumerate(d):
        for j, v in enumerate(r):
            if v != INF and i != j:
                ans = max(ans, v)
    return ans


def main():
    H, W = read_int_n()
    S = [read_str() for _ in range(H)]


    # H = 20
    # W = 20
    # S = ['.'*W]*H
    print(slv(H, W, S))

if __name__ == '__main__':
    main()
