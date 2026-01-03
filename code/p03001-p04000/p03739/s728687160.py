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
def slv(N, A):
    S = [A[0]]
    for a in A[1:]:
        S.append(S[-1]+a)

    def f(sig):
        o = 0
        ans = 0
        for s in S:
            s += o
            if s == 0:
                ans += 1
                o -= sig
            elif sig * s > 0:
                ans += abs(s) + 1
                o -= sig*(abs(s) + 1)
            sig *= -1
        return ans
            
    return min(f(1), f(-1))


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))


if __name__ == '__main__':
    main()
