# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


import sys
sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


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
def slv(R, C, K, RCV):
    V = [[0] * C for _ in range(R)]
    for r, c, v in RCV:
        V[r-1][c-1] = v
    memo = [[[0] * (C+1) for _ in range(R+1)] for __ in range(4)]

    for i in range(R):
        for j in range(C):
            for p in range(4):
                memo[p][i][j+1] = max(memo[p][i][j+1], memo[p][i][j])
                memo[0][i+1][j] = max(memo[0][i+1][j], memo[p][i][j])
                if p != 3:
                    memo[p+1][i][j+1] = max(memo[p+1][i][j+1], memo[p][i][j] + V[i][j])
                    memo[0][i+1][j] = max(memo[0][i+1][j], memo[p][i][j] + V[i][j])

    return max(memo[0][-1])


def main():
    R, C, K = read_int_n()
    RCV = [read_int_n() for _ in range(K)]
    print(slv(R, C, K, RCV))


if __name__ == '__main__':
    main()
