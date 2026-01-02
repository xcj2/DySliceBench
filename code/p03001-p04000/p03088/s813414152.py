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

INF = 2**62-1


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


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N):
    M = 10**9 + 7

    def gp(n):
        prohibit = []
        for c in product('AGCT', repeat=n):
            c = ''.join(c)
            if 'AGC' in c:
                prohibit.append(c)

            for i in range(n-1):
                j = i+1
                l = list(c)
                l[i], l[j] = l[j], l[i]
                if 'AGC' in ''.join(l):
                    prohibit.append(c)
        return set(prohibit)

    p3 = gp(3)
    p4 = gp(4)



    memo = {}
    for c in product('AGCT', repeat=3):
        c = ''.join(c)
        if c not in p3:
            memo[c] = 1

    for _ in range(N-3):
        nm = Counter()
        for c in 'AGCT':
            for k, v in memo.items():
                kk = k + c
                if kk not in p4:
                    nm[kk[1:]] += v
                    nm[kk[1:]] %= M

        memo = nm


    return sum(memo.values()) % M


def main():
    N = read_int()
    print(slv(N))


if __name__ == '__main__':
    main()
