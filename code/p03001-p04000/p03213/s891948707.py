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


def pm(X):
    res = {}
    for i in range(2, int(X ** 0.5) + 1):
        if X % i == 0:
            res[i] = 0
            while X % i == 0:
                X //= i
                res[i] += 1
    if X > 1:
        res[X] = 1
    return res


def solve():
    N = Scanner.int()

    # N!の素因数分解
    M = defaultdict(int)
    for i in range(2, N + 1):
        tmp = i
        for j in range(2, int(i ** 0.5) + 1):
            while tmp % j == 0:
                M[j] += 1
                tmp //= j
        if tmp > 1:
            M[tmp] += 1

    ans = 0

    # 75
    for p in range(2, N+1):
        if M[p] >= 74:
            ans += 1

    # 3 * 25
    # 5 * 25
    for p in range(2, N + 1):
        for q in range(2, N+1):
            if p == q:
                continue
            if M[p] >= 2 and M[q] >= 24:
                ans += 1
            if M[p] >= 4 and M[q] >= 14:
                ans += 1

    # 5 * 5 * 3
    for p in range(2, N+1):
        for q in range(p + 1, N + 1):
            for r in range(2, N + 1):
                if p == r:
                    continue
                if q == r:
                    continue
                if M[p] >= 4 and M[q] >= 4 and M[r] >= 2:
                    ans += 1
    print(ans)


def main():
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
