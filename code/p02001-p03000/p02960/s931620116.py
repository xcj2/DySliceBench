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
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)

@mt
def slv(S):
    M = Mod(10**9 + 7)
    M13 = Mod(13)
    t = [0] * 13
    t[0] = 1
    for i, c in enumerate(reversed(S)):
        if c != '?':
            n = M13.mul(M13.pow(10, i), int(c))
            nt = [0] * 13
            for k in range(13):
                nt[(k+n) % 13] = t[k]
            t = nt
        else:
            nt = [0] * 13
            for j in range(10):
                n = M13.mul(M13.pow(10, i), j)
                for k in range(13):
                    nt[(k+n) % 13] = M.add(nt[(k+n) % 13], t[k])
            t = nt
    return t[5]


def main():
    S = read_str()
    print(slv(S))


if __name__ == '__main__':
    main()
