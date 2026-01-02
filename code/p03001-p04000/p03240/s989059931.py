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
def slv(N, XYH):
    XYH.sort(key=lambda x: x[2], reverse=True)
    MM = 101
    M = [[1] * MM for _ in range(MM)]
    for r, (x, y, h) in enumerate(XYH):
        if h == 0:
            M[x][y] = 0
            continue
        for i in range(MM):
            for j in range(MM):
                t = abs(i-x) + abs(j - y) + h
                if r == 0:
                    M[i][j] = t
                else:
                    if M[i][j] != t:
                        M[i][j] = 0

    

    for i in range(MM):
        for j in range(MM):
            if M[i][j] != 0:
                if i > 0 and M[i-1][j] != 0:
                    continue
                if i < MM -1 and M[i+1][j] != 0:
                    continue
                if j > 0 and M[i][j-1] != 0:
                    continue
                if j < MM -1 and M[i][j+1] != 0:
                    continue
                return '%d %d %d' % (i, j, M[i][j])

    assert False


def main():
    N = read_int()
    XYH = [read_int_n() for _ in range(N)]
    print(slv(N, XYH))


if __name__ == '__main__':
    main()
