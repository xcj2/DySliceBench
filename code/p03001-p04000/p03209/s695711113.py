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
def slv(N, X):
    @lru_cache(maxsize=None)
    def p(n):
        if n == 0:
            return 1
        return 2*p(n-1) + 1
    
    @lru_cache(maxsize=None)
    def a(n):
        if n == 0:
            return 1
        return 2*a(n-1) + 3
    
    def f(n, x):
        if x == 1:
            return 0
        
        elif x < a(n-1)+1:
            return f(n-1, x-1)
        
        elif x == a(n-1) + 1:
            return p(n-1)

        elif x == a(n-1) + 2:
            return p(n-1) + 1

        elif x < a(n) - 2:
            return p(n) - f(n-1, a(n)-x-1)
        
        else:
            return p(n)
    
    return f(N, X)

# BBPPPBPBPPPBB

def main():
    N, X = read_int_n()
    print(slv(N, X))

    # print(slv(2, 13))
    # # for i in range(1, 14):
    # #     print(i, slv(2, i))


if __name__ == '__main__':
    main()
