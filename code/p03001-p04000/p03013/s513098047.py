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


class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)


m = Mod(10**9 + 7)


def slv(N, M, A):
    dp = [0] * (N+3)
    b = [False] * (N+3)
    for a in A:
        b[a] = True

    dp[0] = 1
    for i in range(N):
        if not b[i+1]:
            dp[i+1] = m.add(dp[i+1], dp[i])
        if not b[i+2]:
            dp[i+2] = m.add(dp[i+2], dp[i])
    return dp[N]


def main():
    N, M = read_int_n()
    A = [read_int() for _ in range(M)]
    print(slv(N, M, A))


if __name__ == '__main__':
    main()
