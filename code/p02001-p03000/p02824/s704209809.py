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
def slv(N, M, V, P, A):
    A.sort(reverse=True)
    def f(i):
        if i < P:
            return 0

        if V - P <= 0:
            if A[i] + M >= A[P-1]:
                return 0
            else:
                return 1
        else:
            am = A[i] + M
            r = V - P
            B = []
            for j in range(P-1, N):
                if j != i:
                    B.append(A[j])
                j += 1
            heapq.heapify(B)
            C = []
            rm = M * r
            while B:
                b = heapq.heappop(B)
                d  = am - b
                if d > 0:
                    if d > M:
                        d = M
                    if d <= rm:
                        rm -= d
                        C.append(b+d)
                    else:
                        C.append(b+rm)
                        rm = 0
                else:
                    C.append(b)
            return 0 if max(C) <= am and rm == 0 else 1

    b = Bisect(f)
    i = b.bisect_right(0.5, lo=0, hi=N)
    return i


def main():
    N, M, V, P = read_int_n()
    A = read_int_n()
    print(slv(N, M, V, P, A))

    # N = 10**5
    # M = random.randint(0, 10**9)
    # V = random.randint(1, N-1)
    # P = random.randint(1, N-1)
    # A = [random.randint(0, 10**9) for _ in range(N)]
    # print(slv(N, M, V, P, A))


if __name__ == '__main__':
    main()
