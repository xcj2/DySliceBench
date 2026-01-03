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

sys.setrecursionlimit(10000)


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
def slv(N, A):
    sa = sum(A)
    M = N*(N+1)//2
    if sa % M != 0:
        return 'NO'

    k = sa // M

    kk = k
    for i in range(N):
        b = A[(i+1) % N] - A[i]
        b -= k
        if b > 0:
            error_print('a')
            return 'NO'
        if b % N != 0:
            error_print('b')
            return 'NO'
        kk += b // N

    if kk != 0:
        error_print('c')
        return 'NO'

    return 'YES'


def main():
    N = read_int()
    A = read_int_n()
    # N = 10
    # A = [random.randint(1, 10**9) for _ in range(N)]
    # print(A)
    print(slv(N, A))


if __name__ == '__main__':
    main()
