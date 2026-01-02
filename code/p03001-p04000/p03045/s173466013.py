# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


class UnionFind():
    def __init__(self):
        self.__table = {}
        self.__size = defaultdict(lambda: 1)

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
        if x != y:
            self.__size[y] += self.__size[x]
            self.__table[x] = y

    def size(self, x):
        return self.__size[self.__root(x)]

    def table(self):
        return self.__table


@mt
def slv(N, M, XYZ):
    uf = UnionFind()
    for x, y, _ in XYZ:
        uf.union(x, y)

    t = uf.table()
    ans = len(set(v for k, v in t.items() if k == v))
    for i in range(1, N+1):
        if i not in t:
            ans += 1
    return ans


def main():
    N, M = read_int_n()
    XYZ = [read_int_n() for _ in range(M)]
    print(slv(N, M, XYZ))


if __name__ == '__main__':
    main()
