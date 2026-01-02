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
INF = 2**62-1

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


def eratosthenes(n):
    p = []
    t = [-1] * n

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if t[i] == -1:
            p.append(i)
            t[i] = i
            for j in range(2*i, n, i):
                if t[j] == -1:
                    t[j] = i

    for j in range(i+1, n):
        if t[j] == -1:
            p.append(j)
            t[j] = j

    return p, t

P, T = eratosthenes(10**6+1)

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

def factor(a):
    ps = Counter()
    while a != 1:
        f = T[a]
        while a % f == 0:
            ps[f] += 1
            a //= f
    return ps

@mt
def slv(N, A):
    lcm = Counter()
    for a in A:
        ps = factor(a)
        for k in ps.keys():
            lcm[k] = max(lcm[k], ps[k])

    M = Mod(10**9+7)
    l = 1
    for k, v in lcm.items():
        l = M.mul(l, M.pow(k, v))

    ans = 0
    for a in A:
        ans = M.add(ans, M.div(l, a))
    return ans


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))


if __name__ == '__main__':
    main()
