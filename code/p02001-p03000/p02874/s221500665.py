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
def slv(N, LR):
    LR.sort(key=lambda x: x[1])
    LR.sort(key=lambda x: x[0])


    lc = []
    l = 0
    r = INF
    for i in range(N):
        l_, r_ = LR[i]
        l = max(l, l_)
        r = min(r, r_)
        lc.append((l, r))
    
    rc = []
    l = 0
    r = INF
    for i in range(N-1, -1, -1):
        l_, r_ = LR[i]
        l = max(l, l_)
        r = min(r, r_)
        rc.append((l, r))
    
    def c(l, r):
        return max(0, r-l+1)

    ans = 0
    for i in range(N-1):
        ans = max(ans, c(*lc[i]) + c(*rc[N-1-1-i]))
    for i in range(N):
        tmp = c(*LR[i])
        l, r = (0, INF)
        if i != 0:
            l = max(l, lc[i-1][0])
            r = min(r, lc[i-1][1])
        if i != N-1:
            l = max(l, rc[N-1-i][0])
            r = min(r, rc[N-1-i][1])
            
        tmp += c(l, r)
        ans = max(ans, tmp)

    return ans


def main():
    N = read_int()
    LR = [read_int_n() for _ in range(N)]
    print(slv(N, LR))


if __name__ == '__main__':
    main()
