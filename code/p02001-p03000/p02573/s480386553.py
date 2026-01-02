# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()

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
def slv(N, M, AB):
    uf = UnionFind()
    p = set()
    for a, b in AB:
        uf.union(a, b)
        p.add(a)
        p.add(b)

    ans = 1
    for c in p:
        ans = max(ans, uf.size(c))
    return ans


def main():
    N, M = read_int_n()
    AB = [read_int_n() for _ in range(M)]
    print(slv(N, M, AB))


if __name__ == '__main__':
    main()
