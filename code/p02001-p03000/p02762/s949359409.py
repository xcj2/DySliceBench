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
        return self.__table[x]

    def same(self, x, y):
        return self.__root(x) == self.__root(y)

    def union(self, x, y):
        x = self.__root(x)
        y = self.__root(y)
        if self.size(x) > self.size(y):
            x, y = y, x
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
def slv(N, M, K, AB, CD):
    f = UnionFind()
    for a, b in AB:
        f.union(a, b)

    direct = defaultdict(int)
    for a, b in AB:
        direct[a] += 1
        direct[b] += 1
    block = defaultdict(set)
    for c, d in CD:
        block[c].add(d)
        block[d].add(c)


    ans = []
    for i in range(1, N+1):
        cand = f.size(i)
        for u in block[i]:
            if f.same(i, u):
                cand -= 1
        cand -= direct[i]
        cand -= 1
        ans.append(cand)
    return ans



def main():
    N, M, K = read_int_n()
    AB = [read_int_n() for _ in range(M)]
    CD = [read_int_n() for _ in range(K)]
    print(*slv(N, M, K, AB, CD))

if __name__ == '__main__':
    main()
