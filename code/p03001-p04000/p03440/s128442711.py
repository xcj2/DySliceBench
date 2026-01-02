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
input = sys.stdin.readline
INF = 2**62-1

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

    def root(self, x):
        return self.__root(x)

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

    def num_of_group(self):
        g = 0
        for k, v in self.__table.items():
            if k == v:
                g += 1
        return g


@mt
def slv(N, M, A, XY):
    uf = UnionFind()

    for x, y in XY:
        uf.union(x, y)

    d = defaultdict(list)
    for i in range(N):
        d[uf.root(i)].append(A[i])

    for v in d.values():
        heapq.heapify(v)

    if len(d) == 1:
        return 0
    ans = 0
    n = []
    for v in d.values():
        ans += heapq.heappop(v)
        n.extend(v)

    e = len(d)-2
    n.sort()
    if len(n) < e:
        return 'Impossible'
    ans += sum(n[:e])
    return ans


def main():
    N, M = read_int_n()
    A = read_int_n()
    XY = [read_int_n() for _ in range(M)]
    print(slv(N, M, A, XY))


if __name__ == '__main__':
    main()
