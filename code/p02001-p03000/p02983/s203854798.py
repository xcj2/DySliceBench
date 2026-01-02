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


def slv(L, R):
    if R -L > 2019:
        return 0
    ans = sys.maxsize
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            ans = min((i*j) % 2019, ans)
    return ans

@mt
def slv2(L, R):
    ans = sys.maxsize
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            if ans > (i*j) % 2019:
                print(i, j)
            ans = min((i*j)%2019, ans)
    return ans

def main():
    L, R = read_int_n()
    print(slv(L, R))

if __name__ == '__main__':
    main()
