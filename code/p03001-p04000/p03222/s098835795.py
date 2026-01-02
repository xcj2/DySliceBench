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
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]


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
    H, W, K = Scanner.map_int()

    L = []
    for i in range(1 << (W - 1)):
        l = [False for _ in range(W - 1)]
        for j in range(W-1):
            if i >> j & 1:
                l[j] = True
        for j in range(W - 2):
            if l[j] and l[j + 1]:
                break
        else:
            L.append(l)

    m = [[0 for _ in range(W)]for _ in range(W)]
    if W == 1:
        m[0][0] = 1
    else:
        for l in L:
            for w in range(W):
                k = w
                if w < W - 1 and l[w]:
                    k = k + 1
                elif w - 1 >= 0 and l[w - 1]:
                    k = k - 1
                m[w][k] += 1
    dp = [[0 for _ in range(W)]for _ in range(H + 1)]
    dp[0][0] = 1

    for h in range(H):
        for w in range(W):
            for i in range(W):
                dp[h + 1][w] += m[w][i] * dp[h][i]
                dp[h + 1][w] %= MOD
    print(dp[H][K - 1])


def main():
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
