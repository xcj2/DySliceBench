# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from functools import lru_cache
import bisect
import re
import queue
from decimal import *


class Scanner():
    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [input() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [int(input()) for i in range(n)]


class Math():
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Math.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return (a * b) // Math.gcd(a, b)

    @staticmethod
    def divisor(n):
        res = []
        i = 1
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
        return res

    @staticmethod
    def round_up(a, b):
        return -(-a // b)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3, d + 1, 2):
            if n % i == 0:
                return False
        return True


def pop_count(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


MOD = int(1e09) + 7
INF = int(1e15)


def solve():
    H, W = Scanner.map_int()
    S = Scanner.string_list(H)
    dp = [[0 for _ in range(W)] for _ in range(H)]
    if S[0][0] == '#':
        dp[0][0] = 1
    for w in range(W - 1):
        dp[0][w + 1] = dp[0][w] + (S[0][w + 1] != S[0][w])
    for h in range(H - 1):
        dp[h + 1][0] = dp[h][0] + (S[h + 1][0] != S[h][0])
    for h in range(H - 1):
        for w in range(W - 1):
            s = dp[h][w + 1] + (S[h + 1][w + 1] != S[h][w + 1])
            t = dp[h + 1][w] + (S[h + 1][w + 1] != S[h + 1][w])
            dp[h + 1][w + 1] = min(s, t)

    print(Math.round_up(dp[H - 1][W - 1], 2))


def main():
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
