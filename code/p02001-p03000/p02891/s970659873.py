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


MOD = int(1e09) + 7
INF = int(1e15)


def calc(N):
    return sum(int(x) for x in str(N))


def main():
    # sys.stdin = open("sample.txt")
    S = Scanner.string()
    K = Scanner.int()
    if len(Counter(S)) == 1:
        print(len(S) * K // 2)
        return
    ans = 0
    if S[0] == S[-1]:
        c1 = 1
        for i in range(1, len(S)):
            if S[i] == S[0]:
                c1 += 1
            else:
                break
        c2 = 1
        for j in reversed(range(len(S)-1)):
            if S[j] == S[-1]:
                c2 += 1
            else:
                break
        ans = c1 // 2
        ans += c2 // 2
        ans += (c1 + c2) // 2 * (K-1)
        c3 = 0
        c = ""
        for k in range(i, j + 1):
            if S[k] == c:
                c3 += 1
            else:
                ans += c3 // 2 * K
                c = S[k]
                c3 = 1
        ans += c3 // 2 * K
        print(ans)
        return
    else:
        c = "0"
        cnt = 0
        for i in range(len(S)):
            if c == S[i]:
                cnt += 1
            else:
                ans += cnt // 2
                c = S[i]
                cnt = 1
        ans += cnt // 2
        print(ans * K)
    return


if __name__ == "__main__":
    main()
