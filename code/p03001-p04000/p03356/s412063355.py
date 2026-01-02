import math
import random
import heapq
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING
from functools import lru_cache, reduce
from itertools import combinations_with_replacement, product, combinations


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


def read_str_n():
    return list(map(str, input().split()))


def mt(f):
    import time
    import sys

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        print(e - s, 'sec', file=sys.stderr)
        return ret

    return wrap


class UnionFind():
    def __init__(self):
        self.__table = {}

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
            self.__table[x] = y


@mt
def slv(N, M, P, XY):
    P = [-1] + P
    # G = [i for i in range(N + 1)]

    uf = UnionFind()
    for x, y in XY:
        uf.union(x, y)

    ans = 0
    for i, p in enumerate(P):
        if uf.same(p, i):
            ans += 1

    return ans


def main():
    N, M = read_int_n()
    P = read_int_n()
    XY = []
    for _ in range(M):
        XY.append(read_int_n())

    print(slv(N, M, P, XY))


if __name__ == '__main__':
    main()