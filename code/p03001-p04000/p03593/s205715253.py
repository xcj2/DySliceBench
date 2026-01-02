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


@mt
def slv(H, W, M):
    C = Counter()
    for r in M:
        C.update(r)
    f = (H // 2) * (W // 2)
    t = (H % 2) * (W // 2) + (H // 2) * (W % 2)

    v = list(map(lambda x: -x, C.values()))
    heapq.heapify(v)
    for _ in range(f):
        c = -heapq.heappop(v)
        if c == 4:
            pass
        elif c > 4:
            c -= 4
            heapq.heappush(v, -c)
        else:
            return 'No'

    for _ in range(t):
        c = -heapq.heappop(v)
        if c == 2:
            pass
        elif c > 2:
            c -= 2
            heapq.heappush(v, -c)
        else:
            return 'No'
    return 'Yes'


def main():
    H, W = read_int_n()
    M = [read_str() for _ in range(H)]
    print(slv(H, W, M))


if __name__ == '__main__':
    main()
