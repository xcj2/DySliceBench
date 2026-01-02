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


class Bisect:
    def __init__(self, func):
        self.__func = func

    def bisect_left(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if self.__func(mid) < x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def bisect_right(self, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if x < self.__func(mid):
                hi = mid
            else:
                lo = mid+1
        return lo

@mt
def slv(N, M, A):
    P = []
    Z = 0
    N = []
    for a in A:
        if a == 0:
            Z += 1
        elif a < 0:
            N.append(a)
        else:
            P.append(a)
    N.sort()
    P.sort()

    NN = len(N) * len(P)
    ZN = len(N) * Z + len(P) * Z + Z * (Z-1) // 2
    if M <= NN:
        N.reverse()
        def f(n):
            ans = 0
            i = bisect.bisect_left(P, -(n // -N[0]))
            for nn in N:
                m = -(n // -nn)
                while i != 0 and P[i-1] >= m:
                    i -= 1
                ans += len(P) - i
            return ans
        bs = Bisect(f)

        return bs.bisect_right(M-1, -INF, 0)

    elif M <= NN + ZN:
        return 0
    else:
        M -= NN + ZN
        N = [-v for v in N]
        N.sort()

        def f(n):
            ans = 0
            if N:
                i = bisect.bisect_right(N, n//N[0])
                for nn in N:
                    m = n // nn
                    while i != 0 and N[i-1] > m:
                        i -= 1
                    ans += i
                    if i > 0 and N[i-1] >= nn:
                        ans -= 1
            if P:
                i = bisect.bisect_right(P, n//P[0])
                for pn in P:
                    m = n // pn
                    while i != 0 and P[i-1] > m:
                        i -= 1
                    ans += i
                    if i > 0 and P[i-1] >= pn:
                        ans -= 1
            ans //= 2
            return ans
        bs = Bisect(f)
        return bs.bisect_right(M-1, 1, INF)

def f(N, M, A):
    ans = []
    for i in range(N):
        for j in range(i+1, N):
            ans.append((A[i]*A[j], A[i], A[j]))
    ans.sort()
    for i, r in enumerate(ans):
        print(i, r)

def main():
    N, M = read_int_n()
    A = read_int_n()
    print(slv(N, M, A))


if __name__ == '__main__':
    main()
