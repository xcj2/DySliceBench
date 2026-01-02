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
INF = 2**62-1

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
def slv(N, X, Y):
    ans = 0


    c = Counter()
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            a = j - i
            b = abs(i-X) + 1 + abs(j-Y)
            c[min(a, b)] += 1


    for k in range(1, N):
        print(c[k])


    return ans


def main():
    N, X, Y = read_int_n()
    (slv(N, X, Y))

    # N = 2 * (10**3)
    # X = 1000
    # Y = 1500
    # (slv(N, X, Y))



if __name__ == '__main__':
    main()
