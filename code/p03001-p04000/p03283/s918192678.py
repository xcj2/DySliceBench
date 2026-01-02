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


class RectangleSum():
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.s = [[0] * (M+1) for _ in range(N+1)]

    def add(self, i, j, v):
        self.s[i+1][j+1] += v

    def build(self):
        for i in range(self.N+1):
            for j in range(self.M):
                self.s[i][j+1] += self.s[i][j]

        for i in range(self.N):
            for j in range(self.M+1):
                self.s[i+1][j] += self.s[i][j]

    def sum(self, i, j, h, w):
        ret = self.s[i][j]
        ret += self.s[i+h][j+w]
        ret -= self.s[i+h][j]
        ret -= self.s[i][j+w]

        return ret


@mt
def slv(N, M, Q, LR, PQ):
    rs = RectangleSum(N+1, N+1)
    for l, r in LR:
        rs.add(l, r, 1)

    rs.build()

    for p, q in PQ:
        print(rs.sum(p, p, q-p+1, q-p+1))


def main():
    N, M, Q = read_int_n()
    LR = [read_int_n() for _ in range(M)]
    PQ = [read_int_n() for _ in range(Q)]
    slv(N, M, Q, LR, PQ)


if __name__ == '__main__':
    main()
