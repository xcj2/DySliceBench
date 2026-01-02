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
def slv(N):
    E = []
    
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if N % 2 == 0 and i+j == N+1:
                continue
            if N % 2 == 1 and i+j == N:
                continue
            E.append((i, j))

    return E


def main():
    N = read_int()
    E = slv(N)
    print(len(E))
    for e in E:
        print('%d %d' % e)


if __name__ == '__main__':
    main()
