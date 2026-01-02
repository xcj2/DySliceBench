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
from operator import add, mul

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
    return input()


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
def slv(S):
    dp = [0] * 4
    MOD = 10**9 + 7
    dp[0] = 1
    for c in S:
        if c == '?':
            for i in range(3, 0, -1):
                dp[i] = dp[i]*3 + dp[i-1]
                dp[i] %= MOD
            dp[0] = dp[0]*3
            dp[0] %= MOD
        elif c == 'A':
            dp[1] += dp[0] % MOD
        elif c == 'B':
            dp[2] += dp[1] % MOD
        elif c == 'C':
            dp[3] += dp[2] % MOD
    return dp[3] % MOD


def main():
    S = read_str().strip()
    print(slv(S))


if __name__ == '__main__':
    main()
