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
def slv(N, K, X):

    ans = sys.maxsize
    for i in range(N-K+1):
        c = 0
        if X[i] <= 0 and X[i+K-1] <= 0:
            c += -X[i]
        elif X[i] <= 0 and X[i+K-1] > 0:
            c += -2*X[i] + X[i+K-1]
        else:
            c += X[i+K-1]

        # print(c)
        ans = min(ans, c)

    X = [-x for x in reversed(X)]
    for i in range(N-K+1):
        c = 0
        if X[i] <= 0 and X[i+K-1] <= 0:
            c += -X[i]
        elif X[i] <= 0 and X[i+K-1] > 0:
            c += -2*X[i] + X[i+K-1]
        else:
            c += X[i+K-1]

        # print(c)
        ans = min(ans, c)
    return ans


def main():
    N, K = read_int_n()
    X = read_int_n()
    print(slv(N, K, X))


if __name__ == '__main__':
    main()
