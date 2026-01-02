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
def slv(A, B, X):
    for x in X:
        i = bisect.bisect_left(A, x)
        la = A[i-1] if i > 0 else sys.maxsize
        ra = A[i] if i < len(A) else sys.maxsize

        i = bisect.bisect_left(B, x)
        lb = B[i-1] if i > 0 else sys.maxsize
        rb = B[i] if i < len(B) else sys.maxsize

        # print(x, la, ra, lb, rb, abs(rb-x))
        e =  max(abs(x-la), abs(x-lb)) 
        f =  max(abs(ra-x), abs(rb-x))
        g = min(abs(la-x), abs(rb-x))*2 + max(abs(la-x), abs(rb-x))
        h = min(abs(ra-x), abs(lb-x))*2 + max(abs(ra-x), abs(lb-x))
        print(min(e, f, g, h))


def main():
    # N = read_int()
    AN, BN, Q = read_int_n()
    A = [read_int() for _ in range(AN)]
    B = [read_int() for _ in range(BN)]
    X = [read_int() for _ in range(Q)]
    slv(A, B, X)


if __name__ == '__main__':
    main()
