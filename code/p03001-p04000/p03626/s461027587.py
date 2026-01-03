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
def slv(N, S1, S2):
    ans = 0
    MOD = 1000000007

    if S1[0] == S2[0]:
        ans = 3
        i = 1
        p = 0
    else:
        ans = 6
        i = 2
        p = 1

    while i < N:
        if p == 0:
            if S1[i] == S2[i]:
                ans *= 2
                i += 1
                p = 0
            else:
                ans *= 2
                i += 2
                p = 1
        else:
            if S1[i] == S2[i]:
                p = 0
                i += 1
            else:
                ans *= 3
                i += 2
                p = 1
        ans %= MOD

    return ans


def main():
    N = read_int()
    S1 = read_str()
    S2 = read_str()

    print(slv(N, S1, S2))


if __name__ == '__main__':
    main()
