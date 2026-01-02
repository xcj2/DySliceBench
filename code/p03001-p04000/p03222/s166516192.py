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



def C(n, r):
    c = 1
    for i in range(1, r+1):
        c *= n
        c //= i
        n -= 1

    return c

@mt
def slv(H, W, K):
    dp = [[0] * (W+2) for _ in range(H+1)]

    
    L = [0] * (W+2)
    C = [0] * (W+2)
    R = [0] * (W+2)
    for c in product(range(2), repeat=W-1):
        for i in range(W-2):
            if c[i] * c[i+1] != 0:
                break
        else:
            for j in range(1, W+1):
                if j != 1 and c[j-2] == 1:
                    L[j] += 1
                elif j != W and c[j-1] == 1:
                    R[j] += 1
                else:
                    C[j] += 1

    dp[0][1] = 1
    mod = 10**9 + 7
    for h in range(0, H):
        for w in range(1, W+1):
            dp[h+1][w-1] += dp[h][w] * L[w]
            dp[h+1][w-1] %= mod
            dp[h+1][w] += dp[h][w] * C[w]
            dp[h+1][w] %= mod
            dp[h+1][w+1] += dp[h][w] * R[w]
            dp[h+1][w+1] %= mod


    return dp[H][K]


def main():
    H, W, K = read_int_n()
    # A = [read_int_n() for _ in range(N)]
    print(slv(H, W, K))


if __name__ == '__main__':
    main()
