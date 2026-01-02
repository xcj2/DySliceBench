# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul

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
    return input()


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


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def slv2(A, B, C, D):
    if A < B:
        return 'No'

    if D < B:
        return 'No'

    if C >= B:
        return 'Yes'

    g = gcd(B, D)
    if B - g + (A % g) > C:
        return 'No'

    return 'Yes'


@mt
def slv(T, Q):
    a = []
    for q in Q:
        a.append(slv2(*q))

    return '\n'.join(a)


def main():

    T = read_int()
    Q = [read_int_n() for _ in range(T)]
    print(slv(T, Q))


if __name__ == '__main__':
    main()
