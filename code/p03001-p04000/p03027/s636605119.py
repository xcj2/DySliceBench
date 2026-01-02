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


def read_int():
    return int(input())


def read_int_n():
    return map(int, input().split())


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


class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)


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


M = 1000003
m = Mod(M)
C = Combination(M-1, M)


def slv(x, d, n):
    if d == 0:
        return m.pow(x, n)

    xd = m.div(x, d)
    if n > M - xd:
        return 0

    return m.mul(m.mul(C.g1[xd+n-1], C.g2[xd-1]), m.pow(d, n))


def main():
    Q = read_int()
    for _ in range(Q):
        x, d, n = read_int_n()
        print(slv(x, d, n))


if __name__ == '__main__':
    main()
