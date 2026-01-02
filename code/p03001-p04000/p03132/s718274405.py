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


@mt
def slv(L, A):

    dp = [[sys.maxsize] * (L+1) for _ in range(5)]
    for i in range(5):
        dp[i][0] = 0

    def s(a, t):
        if t == 0 or t == 4:
            return a
        if t == 1 or t == 3:
            if a == 0:
                return 2
            else:
                return a % 2
        else:
            return (a+1) % 2

    for i, a in enumerate(A):
        for j in range(5):
            if j > 0:
                dp[j][i] = min(dp[j-1][i], dp[j][i])
            dp[j][i+1] = min(dp[j][i+1], dp[j][i]+s(a, j))
        # dp[0][i+1] = dp[0][i] + a
        # dp[1][i+1] = min(dp[0][i], dp[1][i]) + ((a%2) if a != 0 else 2)
        # dp[2][i+1] = min(dp[1][i], dp[2][i]) + ((a+1)%2)
        # dp[3][i+1] = min(dp[2][i], dp[3][i]) + ((a%2) if a != 0 else 2)
        # dp[4][i+1] = min(dp[3][i], dp[4][i]) + a
    

    return min([dp[i][L] for i in range(5)])

def main():
    L = read_int()
    A = [read_int() for _ in range(L)]
    print(slv(L, A))


if __name__ == '__main__':
    main()
