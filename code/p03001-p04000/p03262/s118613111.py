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
def slv(N, S, X):
    Xs = []
    for x in X:
        t = abs(x - S)
        Xs.append(t)

    if N == 1:
        return Xs[0]
    ans = gcd(Xs[0], Xs[1])
    for i in range(2, N):
        ans = gcd(ans, Xs[i])

    return ans


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    N, S = read_int_n()
    X = read_int_n()
    print(slv(N, S, X))

    # N = 10000
    # S = random.randint(1, 10**9)
    # # X = [random.randint(1, 10**9) for _ in range(N)]
    # S = 1
    # X = list(range(N))
    # print(slv(N, S, X))


if __name__ == '__main__':
    main()
