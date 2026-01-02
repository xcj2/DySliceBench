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


def f(n):
    r = 2
    ret = 1
    for i in range(n, n-r, -1):
        ret *= i
    for i in range(1, r+1):
        ret //= i
    return ret * 2 + n


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
    A.sort(reverse=True)
    print(A)
    b = Bisect(f)

    i = b.bisect_left(M, 1, N)
    if f(i) != M:
        i -= 1
    l = f(i)

    ans = 0
    for j in range(i):
        ans += A[j] * 2
        ans += A[j] * (i-1)

    rem = M - l
    print(i, l, rem)
    j = 0
    while rem != 0:
        ans += A[j] + A[i]
        rem -= 1
        if rem == 0:
            break
        ans += A[j] + A[i]
        rem -= 1
        if rem == 0:
            break
        j += 1


    return ans

import numpy as np
@mt
def slv2(N, M, A):
    C = Counter(A)
    L = 1 << (max(A).bit_length() + 1)
    B = [C[i] for i in range(L)]
    D = np.fft.rfft(B)
    D *= D
    E = list(map(int, np.round(np.fft.irfft(D))))
    ans = 0
    c = 0
    i = L - 1

    while c != M:
        n = E[i]
        if c + n > M:
            n = M-c
        c += n
        ans += i * n
        i -= 1

    return ans

def main():
    N, M = read_int_n()
    A = read_int_n()
    print(slv2(N, M,A))

    # N = 10**5
    # M = random.randint(1, N**2)
    # A = [random.randint(1, 10**5) for _ in range(N)]
    # print(slv(N, M, A))


if __name__ == '__main__':
    main()
