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


# @mt
def slv(N, A):
    
    L = [-A.pop(0)]
    ma = L[0]
    for a in A:
        if ma <= -a:
            ma = -a
            L.append(ma)
            continue
        i = bisect.bisect_right(L, -a)
        L[i] = -a
        ma = L[-1]
    return len(L)



def main():
    N = read_int()
    A = [read_int() for _ in range(N)]
    print(slv(N, A))


if __name__ == '__main__':
    main()
