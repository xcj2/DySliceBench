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
def slv(N, M, PY):
    PY = [(p, y, i) for i, (p, y) in enumerate(PY)]
    PY.sort(key=lambda x: x[1])

    id = []
    pc = Counter()
    for p, y, i in PY:
        pc[p] += 1
        id.append(("%06d%06d" % (p, pc[p]), i))

    id.sort(key=lambda x: x[1])
    for s, _ in id:
        print(s)


def main():
    N, M = read_int_n()
    PY = [read_int_n() for _ in range(M)]
    slv(N, M, PY)


if __name__ == '__main__':
    main()
