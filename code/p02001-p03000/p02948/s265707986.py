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
    def roundUp(a, b):
        return -(-a // b)

    @staticmethod
    def toUpperMultiple(a, x):
        return Math.roundUp(a, x) * x

    @staticmethod
    def toLowerMultiple(a, x):
        return (a // x) * x

    @staticmethod
    def nearPow2(n):
        if n <= 0:
            return 0
        if n & (n - 1) == 0:
            return n
        ret = 1
        while(n > 0):
            ret <<= 1
            n >>= 1
        return ret

    @staticmethod
    def sign(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        return 1

    @staticmethod
    def isPrime(n):
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

    @staticmethod
    def divisor(n):
        i = 1
        table = []
        while i * i <= n:
            if n % i == 0:
                table.append(i)
                table.append(n // i)
            i += 1
        table = list(set(table))
        return table


class PriorityQueue:
    def __init__(self, l=[]):
        self.__q = l
        heapq.heapify(self.__q)
        return

    def push(self, n):
        heapq.heappush(self.__q, n)
        return

    def pop(self):
        return heapq.heappop(self.__q)

    def list(self):
        return self.__q

    def length(self):
        return len(self.__q)


sys.setrecursionlimit(1000000)
MOD = int(1e09) + 7
INF = int(1e30)


def main():
    # sys.stdin = open("Sample.txt")
    N, M = Scanner.map_int()
    X = Scanner.int_list_list(N)
    X.sort()
    ans = 0
    tasks = PriorityQueue()
    i = 0
    for t in reversed(range(M)):
        while i < N and X[i][0] + t <= M:
            tasks.push(-X[i][1])
            i += 1
        if tasks.length() > 0:
            ans += -tasks.pop()
    print(ans)
    return


if __name__ == "__main__":
    main()
