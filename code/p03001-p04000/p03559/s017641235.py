# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
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


@mt
def slv(N, A, B, C):
    A.sort()
    B.sort()
    C.sort()

    D = [0] * (N+1)
    for i in range(N-1, -1, -1):
        j = bisect.bisect_right(C, B[i])
        D[i] = D[i+1] + (N-j)

    ans = 0
    for i in range(N-1, -1, -1):
        j = bisect.bisect_right(B, A[i])
        ans += D[j]

    return ans


def main():
    N = read_int()
    A = read_int_n()
    B = read_int_n()
    C = read_int_n()
    print(slv(N, A, B, C))


if __name__ == '__main__':
    main()
