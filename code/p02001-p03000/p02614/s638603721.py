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
def slv(H, W, K, C):
    ans = 0

    for h in range(H+1):
        for w in range(W+1):
            for i in combinations(range(H), r=h):
                i = set(i)
                for j in combinations(range(W), r=w):
                    j = set(j)
                    t = 0
                    for x in range(H):
                        for y in range(W):
                            if x in i or y in j:
                                continue
                            if C[x][y] == '#':
                                t += 1
                    if t == K:
                        ans += 1

    return ans


def main():
    H, W, K = read_int_n()
    C = [read_str() for _ in range(H)]
    print(slv(H, W, K, C))


if __name__ == '__main__':
    main()
