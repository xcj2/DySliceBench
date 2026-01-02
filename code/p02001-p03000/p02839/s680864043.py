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
# sys.setrecursionlimit(10**6)
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
def slv(H, W, A, B):
    C = [[abs(a-b) for a, b in zip(ar, br)] for ar, br in zip(A, B)]

    memo = [[set() for _ in range(W)] for __ in range(H)]
    memo[0][0].add(C[0][0])
    for i in range(H):
        for j in range(W):
            c = C[i][j]
            s = memo[i][j]
            if i > 0:
                for d in memo[i-1][j]:
                    s.add(abs(d + c))
                    s.add(abs(d - c))
            if j > 0:
                for d in memo[i][j-1]:
                    s.add(abs(d + c))
                    s.add(abs(d - c))

    return min(map(abs, memo[H-1][W-1]))




def main():
    H, W = read_int_n()
    A = [read_int_n() for _ in range(H)]
    B = [read_int_n() for _ in range(H)]
    print(slv(H, W, A, B))


if __name__ == '__main__':
    main()
