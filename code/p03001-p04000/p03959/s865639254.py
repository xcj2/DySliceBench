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

    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)

@mt
def slv(N, T, A):

    ft = [False] * N
    ft[0] = True

    for i in range(1, N):
        if T[i-1] < T[i]:
            ft[i] = True

    fa = [False] * N
    fa[-1] = True
    for i in range(N-2, 0, -1):
        if A[i] > A[i+1]:
            fa[i] = True
    
    H = []
    for i in range(N):
        if ft[i] and fa[i]:
            if T[i] != A[i]:
                return 0
        elif ft[i]:
            if T[i] > A[i]:
                return 0
        elif fa[i]:
            if T[i] < A[i]:
                return 0
        else:
            H.append(min(T[i], A[i]))

    M = Mod(10**9+7)
    ans = 1
    for h in H:
        ans = M.mul(ans, h)
    return ans


def main():
    N = read_int()
    T = read_int_n()
    A = read_int_n()
    print(slv(N, T, A))


if __name__ == '__main__':
    main()
