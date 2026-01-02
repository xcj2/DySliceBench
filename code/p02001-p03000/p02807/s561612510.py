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

class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    @lru_cache(maxsize=None)
    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)

@mt
def slv(N, X):
    M = Mod(10**9+7)
    ne = [1]
    for i in range(1, N+1):
        ne.append(M.mul(i, ne[i-1]))
    ans = 0
    p = 0
    for i in range(N-1):
        d = X[i+1] - X[i]
        p = M.add(p, M.div(ne[N-1], i+1))
        ans = M.add(ans, M.mul(d, p))
    return ans

def slv2(N, X):
    ans = 0
    s = Counter()
    for p in permutations(range(N-1)):
        x = X[:]
        for i in p:
            for j in range(i+1, N):
                if x[j]:
                    break

            ans += x[j] - x[i]
            s[(j, i)] += 1
            x[i] = None
    for i in range(N-1):
        for j in range(i+1, N):
            print(i, j, s[(j,i)])
    return ans

def main():
    N = read_int()
    X = read_int_n()
    print(slv(N, X))
    # print(slv2(N, X))

    # N = 10**4
    # X = list(range(1, N+1))
    # print(slv(N, X))


if __name__ == '__main__':
    main()
