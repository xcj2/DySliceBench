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


def dc(n, m):
    return -(-n // m)

# @mt
def slv(H, N, AB):

    dp = [INF] * (H+1)
    dp[0] = 0
    for a, b in AB:
        for h, bb in enumerate(dp):
            if bb == INF:
                continue
            n = min(H, h+a)
            dp[n]  = min(dp[n], bb+b)
    return dp[-1]


def main():
    H, N = read_int_n()
    AB = [read_int_n() for _ in range(N)]
    print(slv(H, N, AB))
    # H = 10**4
    # N = 10
    # AB = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(N)]
    # print(slv(H, N, AB))


if __name__ == '__main__':
    main()
