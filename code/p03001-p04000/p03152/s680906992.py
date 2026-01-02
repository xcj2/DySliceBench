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
def slv(N, M, A, B):
    
    mod = 10**9 + 7

    if len(A) != len(set(A)):
        return 0
    if len(B) != len(set(B)):
        return 0
    
    A.sort()
    B.sort()
    As = set(A)
    Bs = set(B)

    ans = 1
    NM = N*M
    for i in range(N*M, 0, -1):
        if i in As and i in Bs:
            pass
        elif i in As:
            j = M - bisect.bisect_right(B, i)
            ans = (ans * j) % mod
        elif i in Bs:
            j = N - bisect.bisect_right(A, i)
            ans = (ans * j) % mod
        else:
            j = N - bisect.bisect_right(A, i)
            k = M - bisect.bisect_right(B, i)
            ans = (ans * (j*k-(NM-i))) % mod

    
    return ans


def main():
    N, M = read_int_n()
    A = read_int_n()
    B = read_int_n()
    print(slv(N, M, A, B))


if __name__ == '__main__':
    main()
