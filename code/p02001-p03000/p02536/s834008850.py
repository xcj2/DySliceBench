# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


class UnionFind():
    def __init__(self):
        self.__table = {}
        self.__size = defaultdict(lambda: 1)
        self.__rank = defaultdict(lambda: 1)

    def __root(self, x):
        if x not in self.__table:
            self.__table[x] = x
            return x
        else:
            a = x
            ul = []
            while a != self.__table[a]:
                ul.append(a)
                a = self.__table[a]
            for u in ul:
                self.__table[u] = a

        return self.__table[x]

    def same(self, x, y):
        return self.__root(x) == self.__root(y)

    def union(self, x, y):
        x = self.__root(x)
        y = self.__root(y)
        if x == y:
            return False

        if self.__rank[x] < self.__rank[y]:
            self.__table[x] = y
            self.__size[y] += self.__size[x]
        else:
            self.__table[y] = x
            self.__size[x] += self.__size[y]
            if self.__rank[x] == self.__rank[y]:
                self.__rank[x] += 1
        return True

    def size(self, x):
        return self.__size[self.__root(x)]

    def num_of_group(self):
        g = 0
        for k, v in self.__table.items():
            if k == v:
                g += 1
        return g



@mt
def slv(N, M, AB):
    uf = UnionFind()
    for i in range(1, N+1):
        uf.union(i, i)
    for a, b in AB:
        uf.union(a, b)

    return uf.num_of_group() - 1


def main():
    N, M = read_int_n()
    AB = [read_int_n() for _ in range(M)]
    print(slv(N, M, AB))


if __name__ == '__main__':
    main()
