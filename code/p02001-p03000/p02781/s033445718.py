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
def slv(N, K):
    N = int(N)
    @lru_cache(maxsize=None)
    def f(n, k):
        if k == 0:
            return 1
        m = n % 10
        l = n // 10
        if l == 0 and k == 1:
            return m
        elif l == 0:
            return 0
        return f(l, k-1)*m + f(l-1, k-1)*(9-m) + f(l, k)


    return f(N, K)


def f(N, K):
    M = len(N)
    N = int(N)
    ans = 0
    for i in range(N+1):
        n = str(i).count('0')
        if len(str(i)) - n == K:
            ans += 1
            # print(i)
    return ans

def main():
    N = read_str()
    K = read_int()
    print(slv(N, K))

    # print(f(N, K))

    # for _ in range(1000):
    #     N = str(random.randint(1, 100))
    #     K = random.randint(1, 3)
    #     # print(N)
    #     # print(K)
    #     a = slv(N, K)
    #     b = f(N, K)
    #     if a != b:
    #         print(N)
    #         print(K)
    #         print(a, b)
    #         assert a == b



if __name__ == '__main__':
    main()
