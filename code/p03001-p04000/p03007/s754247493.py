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
def slv(N, A):
    A.sort()
    M = A.pop()
    m = A.pop(0)

    ans = []
    while A:
        a = A.pop()
        if a < 0:
            ans.append((M, a))
            M -= a
        else:
            ans.append((m, a))
            m -= a

    print(M-m)
    for x, y in ans:
        print(x, y)
    print(M, m)


def main():
    N = read_int()
    A = read_int_n()
    (slv(N, A))


if __name__ == '__main__':
    main()
