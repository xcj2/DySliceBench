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


class ModInt:
    def __init__(self, x=0, M=10**9+7):
        self.m = M
        self.x = x % self.m

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x, self.m) if isinstance(other, ModInt) else
            ModInt(self.x + other, self.m)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x, self.m) if isinstance(other, ModInt) else
            ModInt(self.x - other, self.m)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x, self.m) if isinstance(other, ModInt) else
            ModInt(self.x * other, self.m)
        )

    def __truediv__(self, other):
        return (
            ModInt(self.x * pow(other.x, self.m - 2, self.m)) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, self.m - 2, self.m))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, self.m)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, self.m))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x, self.m) if isinstance(other, ModInt) else
            ModInt(other - self.x, self.m)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(other.x * pow(self.x, self.m - 2, self.m)) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, self.m - 2, self.m))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, self.m)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, self.m))
        )


@mt
def slv(N, K, LR):
    M = 998244353
    memo = [ModInt(0, M)] * (N+2)
    memo[1] = 1
    memo[1+1] = -1
    for i in range(1, N+1):
        memo[i] += memo[i-1]
        for l, r in LR:
            ll = min(N+1, i+l)
            rr = min(N+1, i+r+1)
            memo[ll] += memo[i]
            memo[rr] -= memo[i]

    return memo[N]


def main():
    N, K = read_int_n()
    LR = [read_int_n() for _ in range(K)]
    print(slv(N, K, LR))


if __name__ == '__main__':
    main()
