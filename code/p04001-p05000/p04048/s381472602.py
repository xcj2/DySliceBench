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
def slv(N, X):
    if N % 2 == 0 and X == N//2:
        return 3*X
    ans = 0
    if X > N//2:
        X = N-X

    ans = X

    def f(n, x):
        # print(n, x)
        ans = 0
        ans += n
        n_x = n // x
        ans += 2*n_x*x - x
        if n % x != 0:
            ans += f(x, n - n_x*x)

        # print(n, x, n_x, 2*n_x*x - x, ans)
        return ans

    return ans + f(N-X, X)


def main():
    N, X = read_int_n()
    print(slv(N, X))

  

if __name__ == '__main__':
    main()
