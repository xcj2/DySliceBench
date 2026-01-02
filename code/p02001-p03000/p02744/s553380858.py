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
def slv(N):
    c = 'abcdefghij'
    a = [-1] * N
    a[0] = 0
    def f(a):
        for i in range(N):
            if a[i] == -1:
                break
        else:
            return [a[:]]
        b = max(a[:i])
        ans = []
        for j in range(b+2):
            a[i] = j
            ans.extend(f(a))
            a[i] = -1
        return ans

    for b in f(a):
        print(''.join([c[i] for i in b]))




def main():
    N = read_int()
    (slv(N))


if __name__ == '__main__':
    main()
