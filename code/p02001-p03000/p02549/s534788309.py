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
sys.setrecursionlimit(10**6)
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


class SegmentTree:
    def __init__(self, array, operator, identity_element):
        _len = len(array)
        self.__len = _len
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
        # ep(self.__tree[self.__size:])

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

    def max_right(self, l, f):
        # https://atcoder.jp/contests/practice2/submissions/16636885
        assert 0 <= l <= self.__len
        if l == self.__len:
            return self.__len

        l += self.__size
        sm = self.__ie
        while True:
            while l % 2 == 0:
                l >>= 1
            if not f(self.__op(sm, self.__tree[l])):
                while l < self.__size:
                    l = 2*l
                    if f(self.__op(sm, self.__tree[l])):
                        sm = self.__op(sm, self.__tree[l])
                        l += 1
                return l - self.__size
            sm = self.__op(sm, self.__tree[l])
            l += 1

            if (l & -l) == l:
                break

        return self.__len

    def min_left(self, r, f):
        assert 0 <= r <= self.__len
        if r == 0:
            return 0

        r += self.__size
        sm = self.__ie
        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not f(self.__op(sm, self.__tree[r])):
                while r < self.__size:
                    r = 2*r + 1
                    if f(self.__op(sm, self.__tree[r])):
                        sm = self.__op(sm, self.__tree[r])
                        r -= 1
                return r + 1 - self.__size
            sm = self.__op(sm, self.__tree[r])

            if (r & -r) == r:
                break

        return 0

    def __getitem__(self, key):
        return self.__tree[key + self.__size]



@mt
def slv(N, K, LR):
    M = 998244353
    memo = SegmentTree([0] * (N+1), add, 0)
    memo.update(1, 1)
    for i in range(2, N+1):
        v = 0
        for l, r in LR:
            v += memo.query(max(0, i-r), max(0, i-l+1))
            v %= M
        memo.update(i, v)

    return memo[N]


def main():
    N, K = read_int_n()
    LR = [read_int_n() for _ in range(K)]
    print(slv(N, K, LR))

    # N = 2 * (10**5)
    # p = [random.randint(1, N) for _ in range(20)]
    # p.sort(reverse=True)
    # LR = []
    # K = 10
    # for i in range(1, 11):
    #     LR.append([2*i-1, 2*i])
    # LR.sort()
    # LR[0][0] = 1
    # print(N, K, LR)

    # print(slv(N, K, LR))



if __name__ == '__main__':
    main()
