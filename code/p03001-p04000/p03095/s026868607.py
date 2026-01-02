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
        return (a + b ) % self.m

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



@mt
def slv(N, S):

    ans = 0
    CC = Counter()
    for c in S:
        CC[c] += 1
    
    m = Mod(10**9+7)

    cs = tuple(CC.values())
    @lru_cache(maxsize=None)
    def f(v):
        if not v:
            return 1
        
        c = v[0]
        v = v[1:]
        return m.add(m.mul(c, f(v)), f(v))
    return f(cs) - 1


def main():
    N = read_int()
    S = read_str()
    print(slv(N, S))


if __name__ == '__main__':
    main()
