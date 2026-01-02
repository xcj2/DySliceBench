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
def slv(N, P, S):
    if P == 2 or P == 5:
        n = 0
        ans = 0
        for c in reversed(S):
            if int(c) % P == 0:
                n += 1
            ans += n
        return ans

    p = Counter()
    t = 1
    ans = 0
    c = 0
    for i in range(N):
        a = ((int(S[N-i-1]) * t) + c) % P
        c = a
        if a == 0:
            ans += 1
        ans += p[a]
        p[a] += 1
        t = (t * 10) % P

    return ans


def main():
    N, P = read_int_n()
    S = read_str()
    print(slv(N, P, S))


if __name__ == '__main__':
    main()
