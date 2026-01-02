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
def slv(H, W, S):
    ans = 0
    ph = [[0] * W for _ in range(H)]
    for i in range(H):
        tmp = []
        for j in range(W):
            if S[i][j] == '.':
                tmp.append(j)
            else:
                p = len(tmp)
                for t in tmp:
                    ph[i][t] = p
                tmp = []
        if tmp:
            p = len(tmp)
            for t in tmp:
                ph[i][t] = p
            tmp = []

    pv = [[0] * W for _ in range(H)]
    for i in range(W):
        tmp = []
        for j in range(H):
            if S[j][i] == '.':
                tmp.append(j)
            else:
                p = len(tmp)
                for t in tmp:
                    pv[t][i] = p
                tmp = []
        if tmp:
            p = len(tmp)
            for t in tmp:
                pv[t][i] = p
            tmp = []

    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, ph[i][j] + pv[i][j])

    return ans - 1


def main():
    H, W = read_int_n()
    S = [read_str() for _ in range(H)]
    print(slv(H, W, S))

    # H = 2000
    # W = 2000
    # S = [random.choices('.#', k=W) for _ in range(H)]
    # print(slv(H, W, S))


if __name__ == '__main__':
    main()
