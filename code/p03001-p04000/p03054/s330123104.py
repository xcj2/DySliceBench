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
def slv(H, W, N, s, S, T):
    s_ = s
    lx = 0
    rx = W-1
    ly = 0
    ry = H-1
    for s, t in reversed(list(zip(S, T))):
        if t == 'R':
            lx = max(0, lx-1)
        elif t == 'L':
            rx = min(W-1, rx+1)
        elif t == 'D':
            ly = max(0, ly-1)
        elif t == 'U':
            ry = min(H-1, ry+1)

        if s == 'L':
            lx += 1
        elif s == 'R':
            rx -= 1
        elif s == 'U':
            ly += 1
        elif s == 'D':
            ry -= 1

        if lx > rx:
            return 'NO'
        elif ly > ry:
            return 'NO'

    s = s_
    # print(s, lx, rx, ly, ry)
    if not (lx <= s[1]-1 <= rx):
        return 'NO'
    elif not (ly <= s[0]-1 <= ry):
        return 'NO'
    return 'YES'


def main():
    H, W, N = read_int_n()
    s = read_int_n()
    S = read_str()
    T = read_str()
    print(slv(H, W, N, s, S, T))


if __name__ == '__main__':
    main()
