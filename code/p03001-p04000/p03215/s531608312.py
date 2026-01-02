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
def slv(N, K, A):

    sa = [0]
    for a in A:
        sa.append(sa[-1]+a)
    
    s = []
    for i in range(N+1):
        for j in range(i+1, N+1):
            s.append(sa[j]-sa[i])
    s.sort()


    pool = s
    for b in range(s[-1].bit_length(), -1, -1):
        cnd = []
        v = 1 << b
        for a in pool:
            if a & v > 0:
                cnd.append(a)
        if len(cnd) >= K:
            pool = cnd

    return reduce(lambda x, y: x&y,  pool)

        




def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))


if __name__ == '__main__':
    main()
