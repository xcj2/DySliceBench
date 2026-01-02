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
def slv(A, B, C, D, E, F):
    ans = 0
    w = set()
    for i in range(F//A + 1):
        for j in range(F//B + 1):
            m = 100*(i*A + j*B)
            if m < F:
                w.add(m)
    mw = max(w)


    ms = (mw // 100) * E
    s = set()
    for i in range(ms+1):
        for j in range(ms+1):
            s.add(i*C + j*D)
    W = sorted(w)
    S = sorted(s)

    ans = (0, A*100, 0)
    for w in W:
        if w == 0:
            continue
        ts = w // 100 * E
        if F < ts + w:
            ts = F - w
        si = bisect.bisect_left(S, ts)
        if S[si] == ts:
            s = ts
        else:
            if si == 0:
                continue
            s = S[si-1]
        if s + w <= F and  s / w > ans[0]:
            ans = (s/w, w + s, s)
    return ' '.join(map(str, ans[1:]))


def main():
    A, B, C, D, E, F = read_int_n()
    print(slv(A, B, C, D, E, F))


if __name__ == '__main__':
    main()
