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


@mt
def slv(N, K, XY):
    X = sorted(map(lambda x: x[0], XY))
    RX = X[::-1]
    Y = sorted(map(lambda x: x[1], XY))
    RY = Y[::-1]

    ans = sys.maxsize
    for lx in X:
        for rx in RX:
            if lx > rx:
                break
            for by in Y:
                for ty in RY:
                    if by > ty:
                        break

                    k = 0
                    for x, y in XY:
                        if lx <= x <= rx and by <= y <= ty:
                            k += 1
                    if k >= K:
                        ans = min(ans, (rx-lx)*(ty-by))
                    else:
                        break

    return ans


def main():
    N, K = read_int_n()
    XY = [read_int_n() for _ in range(N)]

    print(slv(N, K, XY))


if __name__ == '__main__':
    main()
