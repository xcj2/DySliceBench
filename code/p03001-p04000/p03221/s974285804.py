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


class City:
    def __init__(self, id, p, y):
        self._id = id
        self._p = p
        self._y = y
        self._x = 0


def main():
    # sys.stdin = open("sample.txt")
    N, M = Scanner.map_int()
    cities = []
    for i in range(M):
        p, x = Scanner.map_int()
        cities.append(City(i, p, x))
    cities.sort(key=lambda c: c._y)
    M = defaultdict(int)
    for c in cities:
        M[c._p] += 1
        c._x = M[c._p]
    cities.sort(key=lambda c: c._id)
    for c in cities:
        print('{:0>6}{:0>6}'.format(c._p, c._x))


if __name__ == "__main__":
    main()
