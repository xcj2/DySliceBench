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


def func(A):
    N = len(A)
    tmp = N // 2
    T = [0 for _ in range(N)]
    for i in range(0, Math.round_up(N, 2)):
        T[tmp] = A[i]
        if i % 2 == 0:
            tmp -= (i + 1) * 2
        else:
            tmp += (i + 1) * 2
    tmp = N // 2 - 1
    for i in range(0, N // 2):
        T[tmp] = A[N - i - 1]
        if i % 2 == 0:
            tmp += (i + 1) * 2
        else:
            tmp -= (i + 1) * 2
    res = 0
    for i in range(N - 1):
        res += abs(T[i + 1] - T[i])
    return res


def solve():
    N = Scanner.int()
    A = [0 for _ in range(N)]
    for i in range(N):
        A[i] = Scanner.int()
    A.sort()
    ans = func(A)
    A.sort(reverse=True)
    ans = max(ans, func(A))
    print(ans)


def main():
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
