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


class Combination:
    def __init__(self, n, mod):

        g1 = [1, 1]
        g2 = [1, 1]
        inverse = [0, 1]
        for i in range(2, n + 1):
            g1.append((g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod//i)) % mod)
            g2.append((g2[-1] * inverse[-1]) % mod)
        self.MOD = mod
        self.N = n
        self.g1 = g1
        self.g2 = g2
        self.inverse = inverse

    def __call__(self, n, r):
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.MOD


@mt
def slv(N, K):
    ans = 0
    M = 10**9 + 7

    C = Combination(N*2+1, M)
    def H(n, r):
        return C(n+r-1, r)

    K = min(N-1, K)
    for k in range(K+1):
        m = N - k
        t = C(N, k) * H(m, k)
        ans += t
        ans %= M

    return ans


def main():
    N, K = read_int_n()
    print(slv(N, K))


if __name__ == '__main__':
    main()
