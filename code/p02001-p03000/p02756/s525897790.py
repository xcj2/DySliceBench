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
def slv(S, Q):
    ans = 0
    S = deque(S)
    r = False
    for q in Q:
        if q[0] =='1':
            r = not r
        else:
            f = q[1]
            c = q[2]
            if f == '1':
                if r:
                    S.append(c)
                else:
                    S.appendleft(c)
            else:
                if r:
                    S.appendleft(c)
                else:
                    S.append(c)
    S = list(S)
    if r:
        S.reverse()
    return ''.join(S)


def main():
    S = read_str()
    N = read_int()
    Q = [read_str_n() for _ in range(N)]
    print(slv(S, Q))


if __name__ == '__main__':
    main()
