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
def slv(N, M, XY):
    rc = [False] * (N + 1)
    bn = [1] * (N + 1)

    rc[1] = True
    for x, y in XY:
        bn[x] -= 1
        bn[y] += 1
        if rc[x]:
            rc[y] = True
        if bn[x] == 0 and rc[x]:
            rc[x] = False

    return rc.count(True)


def main():
    N, M = read_int_n()
    XY = [read_int_n() for _ in range(M)]
    print(slv(N, M, XY))


if __name__ == '__main__':
    main()
