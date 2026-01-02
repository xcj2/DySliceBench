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
def slv(N, V):
    v1 = [v for v in V[::2]]
    v2 = [v for v in V[1::2]]

    v1c = Counter(v1)
    v2c = Counter(v2)
    v1 = v1c.most_common(2)
    v2 = v2c.most_common(2)
    v1.append((-1, 0))
    v2.append((-1, 0))
    v1_1, v1_2 = v1[:2]
    v2_1, v2_2 = v2[:2]

    if v1_1[0] != v2_1[0]:
        return (N//2 - v1_1[1]) + (N//2 - v2_1[1])

    return min(
        (N//2 - v1_1[1]) + (N//2 - v2_2[1]),
        (N//2 - v1_2[1]) + (N//2 - v2_1[1]),
    )


def main():
    N = read_int()
    V = read_int_n()
    print(slv(N, V))


if __name__ == '__main__':
    main()
