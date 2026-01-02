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


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a*b)//gcd(a, b)


@mt
def slv(N, M, S, T):
    if N < M:
        S, T = T, S
        N, M = M, N

    if gcd(N, M) == 1:
        if S[0] != T[0]:
            return -1
        return N * M

    else:
        c = gcd(N, M)
        ans = lcm(N, M)
        for i in range(0, ans, ans//c):
            j = i // (M//c)
            k = i // (N//c)
            error_print(i, j, k)
            if S[j] != T[k]:
                return -1
        return lcm(N, M)


def main():
    N, M = read_int_n()
    S = read_str()
    T = read_str()
    print(slv(N, M, S, T))


if __name__ == '__main__':
    main()
