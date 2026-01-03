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

INF = 2**62-1


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


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        error_print(e - s, 'sec')
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
        elif x != self.__table[x]:
            self.__table[x] = self.__root(self.__table[x])
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
def slv(N, M, L):
    lo = 10**6
    uf = UnionFind()
    for i, l in enumerate(L):
        for j in l:
            uf.union(i, j+lo)

    return 'YES' if all(uf.same(0, i) for i in range(1, N)) else 'NO'


def main():
    N, M = read_int_n()
    L = [map(lambda x: x-1, read_int_n()[1:]) for _ in range(N)]
    print(slv(N, M, L))


if __name__ == '__main__':
    main()
