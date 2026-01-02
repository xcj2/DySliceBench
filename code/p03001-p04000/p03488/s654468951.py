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


move = None
tx = None
ty = None


@mt
def slv(S, x, y):
    tx = x
    ty = y
    move = list(map(lambda x: len(x), S.split('T')))
    xm = [move[0]]
    for i in range(2, len(move), 2):
        xm_ = []
        for x in xm:
            xm_.append(x + move[i])
            xm_.append(x - move[i])
        xm = set(xm_)

    ym = [0]
    for i in range(1, len(move), 2):
        ym_ = []
        for y in ym:
            ym_.append(y + move[i])
            ym_.append(y - move[i])
        ym = set(ym_)

    return 'Yes' if tx in xm and ty in ym else 'No'


def main():
    S = read_str().strip()
    x, y = read_int_n()
    print(slv(S, x, y))


if __name__ == '__main__':
    main()
