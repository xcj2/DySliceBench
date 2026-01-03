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
def slv(N, A, X):
    ans = 0
    Y = [x - A for x in X]
    M = 2*N*50 + 1
    dp = [[0]*M for _ in range(N+1)]

    dp[0][N*50] = 1
    for i in range(1, N+1):
        for j in range(0, M):
            if j - Y[i-1] < 0 or j - Y[i-1] > 2*N*50:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-Y[i-1]]


    return dp[N][N*50] - 1


def main():
    N, A = read_int_n()
    X = read_int_n()
    print(slv(N, A, X))


if __name__ == '__main__':
    main()
