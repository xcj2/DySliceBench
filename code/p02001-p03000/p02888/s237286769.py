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
def slv(N, L):
    L.sort()
    ans = 0
    for i, a in enumerate(L):
        for j in range(i+1, N):
            b = L[j]
            l = max(a-b, b-a)
            r = a+b
            x = bisect.bisect_left(L, l, lo=j+1)
            y = bisect.bisect_left(L, r, lo=j+1)
            ans += y - x
            if x <= j <= y:
                ans -= 1
            if x <= i <= y:
                ans -= 1

    return ans


def main():
    N = read_int()
    L = read_int_n()
    print(slv(N, L))

    # N = 2 * (10**3)
    # L = [random.randint(1, 1000) for _ in range(N)]
    # print(slv(N, L))


if __name__ == '__main__':
    main()
