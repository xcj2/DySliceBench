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
def slv(M, D):
    ans = 0

    for m in range(1, M+1):
        for d in range(1, D+1):
            d = str(d)
            if len(d) > 1:
                d10 = int(d[1])
            else:
                d10 = 0
            d1 = int(d[0])
            if d1 >= 2 and d10 >= 2 and d1 * d10 == m:
                ans += 1
    return ans


def main():
    M, D = read_int_n()
    print(slv(M, D))


if __name__ == '__main__':
    main()
