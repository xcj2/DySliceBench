# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
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
def slv(S):
    N = len(S)
    ans = sys.maxsize
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans = min(ans, max(i+1, N-i-1))

    if ans == sys.maxsize:
        return N
    return ans


def main():
    S = read_str().strip()
    # S = ''.join([random.choice('01') for _ in range(100000)])
    print(slv(S))


if __name__ == '__main__':
    main()
