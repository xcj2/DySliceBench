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
def slv(N, D, X):
    p = set([i**2 for i in range(1, int(math.sqrt(16000)))])
    ans = 0
    for i, j in combinations(range(N), 2):
        d = 0
        for k in range(D):
            d += (X[i][k]-X[j][k])**2
        if d in p:
            ans += 1
    return ans


def main():
    N, D = read_int_n()
    X = [read_int_n() for _ in range(N)]
    print(slv(N, D, X))


if __name__ == '__main__':
    main()
