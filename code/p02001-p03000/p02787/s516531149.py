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
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import copy
import decimal


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


def solve():
    H, N = Scanner.map_int()
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = Scanner.map_int()
    INF = 10 ** 10
    dp = [INF for _ in range(H + 1)]
    dp[0] = 0
    for i in range(H + 1):
        for j in range(N):
            k = max(0, i - A[j])
            dp[i] = min(dp[i], dp[k] + B[j])
    print(dp[H])


def main():
    # sys.setrecursionlimit(1000000)
    # sys.stdin = open("sample.txt")
    solve()


if __name__ == "__main__":
    main()
