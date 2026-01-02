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
    mi = (0, -1)
    for i in range(N):
        mi = max(mi, (A[i-1] + A[i], i, A[i-1], A[i]))


    s = min(mi[2], mi[3])*2

    si = mi[1]
    while True:
        ans = [0] * N
        ans[si] = s
        a = A[:]
        a[si-1] -= s//2
        a[si] -= s//2
        for i in range(1, N):
            ans[(si+i)%N] = a[(si+i-1)%N] * 2
            a[(si+i) % N] -= a[(si+i-1) % N]
            a[(si+i-1) % N] = 0
        
        if a[(si+i) % N] == 0:
            break
        s += a[(si+i) % N]
        if s < 0:
            break

    return ' '.join(map(str, ans))


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))


if __name__ == '__main__':
    main()
