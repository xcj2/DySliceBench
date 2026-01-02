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


@mt
def slv(S):
    h2 = int(S[:2])
    t2 = int(S[2:])
    hm = False
    tm = False
    if 1 <= h2 <= 12:
        hm = True
    if 1 <= t2 <= 12:
        tm = True

    if hm and tm:
        return 'AMBIGUOUS'
    elif hm:
        return 'MMYY'
    elif tm:
        return 'YYMM'
    return 'NA'


def main():
    S = read_str()
    print(slv(S))


if __name__ == '__main__':
    main()
