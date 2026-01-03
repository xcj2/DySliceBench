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


MOD = int(1e09) + 7


def main():
    # sys.stdin = open("sample.txt")
    N, M = Scanner.map_int()

    class Edge():
        def __init__(self, a, b, c):
            self.from_ = a
            self.to_ = b
            self.cost_ = c
    edges = [] * M
    for _ in range(M):
        a, b, c = Scanner.map_int()
        a -= 1
        b -= 1
        edges.append(Edge(a, b, c))
    d = [[int(1e09) for _ in range(N)] for _ in range(N)]
    for e in edges:
        d[e.from_][e.to_] = e.cost_
        d[e.to_][e.from_] = e.cost_
    for i in range(N):
        d[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    visited = [False] * M
    for s in range(N):
        for i, e in enumerate(edges):
            if d[s][e.from_] + e.cost_ == d[s][e.to_]:
                visited[i] = True
            if d[s][e.to_] + e.cost_ == d[s][e.from_]:
                visited[i] = True
    print(visited.count(False))


if __name__ == "__main__":
    main()
