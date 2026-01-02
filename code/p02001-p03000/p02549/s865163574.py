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


class LazySegmentTree():
    def __init__(self, op, e, mapping, composition, im, init_array):
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.im = im

        l = len(init_array)

        def ceil_pow2(n):
            x = 0
            while (1 << x) < n:
                x += 1
            return x
        self.log = ceil_pow2(l)
        self.size = 1 << self.log
        self.d = [e() for _ in range(2*self.size)]
        self.lz = [im() for _ in range(self.size)]

        for i, a in enumerate(init_array):
            self.d[i+self.size] = a

        for i in range(self.size-1, 0, -1):
            self.__update(i)

    def set(self, p, x):
        p += self.size

        for i in range(self.log, 0, -1):
            self.__push(p >> i)

        self.d[p] = x

        for i in range(1, self.log+1):
            self.__update(p >> i)

    def __getitem__(self, p):
        p += self.size
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        if l == r:
            return self.e()

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push(r >> i)

        sml = self.e()
        smr = self.e()

        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1

        return self.op(sml, smr)

    def apply(self, l, r, f):
        if l == r:
            return

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push((r-1) >> i)

        l2, r2 = l, r
        while l < r:
            if l & 1:
                self.__all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.__all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2

        for i in range(1, self.log+1):
            if ((l >> i) << i) != l:
                self.__update(l >> i)
            if ((r >> i) << i) != r:
                self.__update((r-1) >> i)

    def __update(self, k):
        self.d[k] = self.op(self.d[2*k], self.d[2*k+1])

    def __all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def __push(self, k):
        self.__all_apply(2*k, self.lz[k])
        self.__all_apply(2*k+1, self.lz[k])
        self.lz[k] = self.im()


M = 998244353

def e():
    return 0

def op(sl, sr):
    return (sl + sr) % M

def mapping(fl, sr):
    return (fl + sr) % M

def composition(fl, fr):
    return (fl + fr) % M

def im():
    return 0

@mt
def slv(N, K, LR):
    memo = LazySegmentTree(op, e, mapping, composition, im, [0]*(N+1))
    memo.apply(1, 1+1, 1)
    for i in range(1, N+1):
        n = memo[i]
        for l, r in LR:
            ll = min(N+1, i+l)
            rr = min(N+1, i+r+1)
            memo.apply(ll, rr, n)

    return memo[N]


def main():
    N, K = read_int_n()
    LR = [read_int_n() for _ in range(K)]
    print(slv(N, K, LR))


if __name__ == '__main__':
    main()
