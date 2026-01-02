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
def slv(N, H):

    for i in range(1, N):
        if H[i-1] - H[i] > 1:
            return 'No'

    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
    
    for i in range(1, N):
        if H[i-1] > H[i]:
            return 'No'
    
    return "Yes"


def slv2(N, H):

    for i in range(1, N):
        if H[i-1] - H[i] > 1:
            return 'No'

    for i in range(2, N):
        if H[i-2] > H[i-1] > H[i]:
            return 'No'

    return "Yes"


def main():
    N = read_int()
    H = read_int_n()
    print(slv(N, H))

    # N = 5
    # for _ in range(10):
    #     H = [random.randint(1, 3) for _ in range(N)]
    #     H_ = H[:]
    #     if slv(N, H[:]) != slv2(N, H[:]):
    #         print(H_, slv(N, H[:]), slv2(N, H[:]))


if __name__ == '__main__':
    main()
