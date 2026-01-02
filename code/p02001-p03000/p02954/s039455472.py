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
def slv(S):
    N = len(S)
    d = [0] * N
    #  R - L
    r = []
    for i in range(N):
        if S[i] == 'R':
            r.append(i)
        else:
            for j in r:
                d[j] = i if (i - j) % 2 == 0 else i - 1
            r = []
    else:
        for j in r:
            d[j] = i - j
    #  L - R
    l = []
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            l.append(i)
        else:
            for j in l:
                d[j] = i if (j - i) % 2 == 0 else i + 1
            l = []
    else:
        for j in l:
            d[j] = j - i

    ans = [0] * N
    for i in d:
        ans[i] += 1

    return ' '.join(map(str, ans))


def main():
    S = read_str()
    print(slv(S))


if __name__ == '__main__':
    main()
