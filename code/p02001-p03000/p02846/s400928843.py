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
def slv(T1, T2, A1, A2, B1, B2):
    la1 = T1*A1
    la2 = T2*A2
    lb1 = T1*B1
    lb2 = T2*B2

    la = la1 + la2
    lb = lb1 + lb2
    if la == lb:
        return 'infinity'

    if la1 > lb1 and la2 > lb2:
        return 0
    if la1 < lb1 and la2 < lb2:
        return 0

    if la > lb and la1 > lb1:
        return 0

    if la < lb and la1 < lb1:
        return 0


    p = la1 - lb1
    q = la2 - lb2
    if p > q:
        p *= -1
        q *= -1
    ans = -p//(q+p)*2
    if -p % (q+p) != 0:
        ans += 1
    return ans

def main():
    T1, T2 = read_int_n()
    A1, A2 = read_int_n()
    B1, B2 = read_int_n()
    print(slv(T1, T2, A1, A2, B1, B2))


if __name__ == '__main__':
    main()
