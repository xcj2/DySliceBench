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
def slv(N, T, AB):
    AB.sort(key=lambda x: x[0])

    dp = [[0] * (N+1) for _ in range(T)]

    for t in range(T):
        for i in range(len(AB)):
            a, b = AB[i]
            if t >= a:
                dp[t][i] = max(dp[t-a][i-1] + b, dp[t-1][i], dp[t][i-1])
            else:
                dp[t][i] = max(dp[t-1][i], dp[t][i-1])

    B = list(map(lambda x: x[1], AB))
    B.append(0)
    
    dp = dp[-1]
    dp.pop()
    ans = 0
    for i, v in enumerate(dp):
        ans = max(ans, v + max(B[i+1:]))
    return ans


def main():
    N, T = read_int_n()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, T, AB))


if __name__ == '__main__':
    main()
