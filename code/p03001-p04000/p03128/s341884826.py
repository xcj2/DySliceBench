# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
import copy
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
def slv(N, M, A):
    c = [
        -1,
        2, # 1 
        5, # 2
        5, # 3
        4, # 4
        5, # 5
        6, # 6
        3, # 7
        7, # 8
        6, # 9
        ]
    
    if 2 in A and 5 in A:
        A.remove(2)
    if 3 in A and 5 in A:
        A.remove(3)
    if 2 in A and 3 in A:
        A.remove(2)
    if 6 in A and 9 in A:
        A.remove(6)



    dp = [None] * (N+1) 
    dp[N] = 0
    for i in range(N, 0, -1):
        if dp[i] is None:
            continue
        
        for a in A:
            if i - c[a] < 0:
                continue
            
            if dp[i-c[a]] is None or dp[i] * 10 + a > dp[i-c[a]]:
                dp[i-c[a]] =  dp[i] * 10 + a

    return dp[0]


def main():
    # N = read_int()
    N, M = read_int_n()
    A = read_int_n()
    print(slv(N, M, A))


if __name__ == '__main__':
    main()
