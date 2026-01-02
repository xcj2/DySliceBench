# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, X, M):
    ans = 0
    x = X
    x %= M
    s = [x]
    u = set()
    while True:
        x *= x
        x %= M
        s.append(x)
        if x in u:
            break
        u.add(x)

    i = s.index(s[-1])
    if i + 1 >= N:
        return sum(s[:N]) % M

    N -= i
    ans += sum(s[:i])

    s = s[i:]
    s.pop()
    ss = sum(s)
    ans += (N // len(s)) * ss
    ans += sum(s[:N%len(s)])
    return ans


def main():
    N, X, M = read_int_n()
    print(slv(N, X, M))

if __name__ == '__main__':
    main()
