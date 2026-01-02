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


class SegmentTree:
    def __init__(self, array, operator, identity_element):
        _len = len(array)
        self.__op = operator
        self.__size = 1 << (_len - 1).bit_length()
        self.__tree = [identity_element] * self.__size + \
            array + [identity_element] * (self.__size - _len)
        self.__ie = identity_element

        for i in range(self.__size - 1, 0, -1):
            self.__tree[i] = operator(
                self.__tree[i * 2], self.__tree[i * 2 + 1])

    def update(self, i, v):
        i += self.__size
        self.__tree[i] = v
        while i:
            i //= 2
            self.__tree[i] = self.__op(
                self.__tree[i * 2], self.__tree[i * 2 + 1])

    def query(self, l, r):
        """[l, r)
        """
        l += self.__size
        r += self.__size
        ret = self.__ie
        while l < r:
            if l & 1:
                ret = self.__op(ret, self.__tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.__op(ret, self.__tree[r])
            l //= 2
            r //= 2
        return ret

    def __getitem__(self, key):
        return self.__tree[key + self.__size]


@mt
def slv(N, C, XV):
    XV.sort()
    ans = 0
    sf = [(0, 0)]
    stf = SegmentTree([-INF]*N, max, -INF)
    c = 0
    for i, (x, v) in enumerate(XV):
        v = sf[-1][0]+v-(x-c)
        sf.append((v, x))
        stf.update(i, v)
        c = x


    str_ = SegmentTree([-INF]*N, max, -INF)
    sr = [(0, 0)]
    c = 0
    for i, (x, v) in enumerate(reversed(XV)):
        x = C - x
        v = sr[-1][0]+v-(x-c)
        sr.append((v, x))
        str_.update(i, v)
        c = x

    ans = 0
    for i in range(N+1):
        t = sf[i][0] + max(0, str_.query(0, N-i) - sf[i][1])
        ans = max(ans, t)
        t = sr[i][0] + max(0, stf.query(0, N-i) - sr[i][1])
        ans = max(ans, t)
    return ans


def main():
    N, C = read_int_n()
    XV = [read_int_n() for _ in range(N)]
    print(slv(N, C, XV))


if __name__ == '__main__':
    main()
