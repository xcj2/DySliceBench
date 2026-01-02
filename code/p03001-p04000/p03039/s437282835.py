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
        return self.mul(a, self.pow(b, self.m-2))

    def pow(self, x, y):
        if y == 0:
            return 1
        elif y == 1:
            return x % self.m
        elif y % 2 == 0:
            return self.pow(x, y//2)**2 % self.m
        else:
            return self.pow(x, y//2)**2 * x % self.m


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
def slv(N, M, K):
    m = Mod(10**9+7)
    d = Combination(N*M, 10**9+7)(N*M-2, K-2)

    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == N and j == M:
                continue
            if i == N or j == M:
                a = 1
            else:
                a = 2
            ans = m.add(ans, m.mul(i*j*a, m.mul(i + j, d)))
    ans = m.div(ans, 2)

    return ans


def main():
    N, M, K = read_int_n()
    print(slv(N, M, K))


if __name__ == '__main__':
    main()
