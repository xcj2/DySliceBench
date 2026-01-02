from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor
from sys import setrecursionlimit

import heapq
import itertools
import operator


inf = float('inf')


def get_int():
    return int(input())


def get_float():
    return float(input())


def get_str():
    return input().strip()


def get_li():
    return [int(i) for i in input().split()]


def get_lf():
    return [float(f) for f in input().split()]


def get_lc():
    return list(input().strip())


def get_data(n, types):
    if len(types) == 1:
        return [types[0](input()) for _ in range(n)]
    return zip(*(
        [t(x) for t, x in zip(types, input().split())]
        for _ in range(n)
    ))


# inputs
N = 0


def set_inputs():
    global N
    N = get_int()
    return


DIVISOR = 1000000007


def main():
    setrecursionlimit(100000)
    set_inputs()

    # ACG, AGC, GAC, AGGC, AGTC, ATGC
    safe = [0] * (N+1)
    a = [0] * (N+1)
    g = [0] * (N+1)
    ac = [0] * (N+1)
    ag = [0] * (N+1)
    at = [0] * (N+1)
    ga = [0] * (N+1)
    agg = [0] * (N+1)
    agt = [0] * (N+1)
    atg = [0] * (N+1)

    safe[0] = 1
    for i in range(1, N+1):
        s = safe[i-1] * 2
        s += g[i-1] * 2
        s += ac[i-1] * 2
        s += at[i-1] * 2
        s += agg[i-1]
        s += agt[i-1]
        s += atg[i-1]
        safe[i] = s % DIVISOR

        a_ = safe[i-1]
        a_ += a[i-1]
        a_ += ac[i-1]
        a_ += at[i-1]
        a_ += ga[i-1]
        a_ += agt[i-1]
        a[i] = a_ % DIVISOR

        g_ = safe[i-1]
        g_ += g[i-1]
        g_ += agg[i-1]
        g_ += agt[i-1]
        g_ += atg[i-1]
        g[i] = g_ % DIVISOR

        ac[i] = a[i-1]
        ag[i] = ( a[i-1] + ga[i-1]) % DIVISOR
        at[i] = ( a[i-1] + ga[i-1]) % DIVISOR
        ga[i] = ( g[i-1] + ag[i-1] + agg[i-1] + atg[i-1]) % DIVISOR
        agg[i] = ag[i-1]
        agt[i] = ag[i-1]
        atg[i] = at[i-1]

        # dead = ( ac[i-1] + ag[i-1] + ga[i-1] + agg[i-1] + agt[i-1] + atg[i-1]) % DIVISOR
    print((safe[N] + a[N] + g[N] + ac[N] + ag[N] + at[N] + ga[N] + agg[N] + agt[N] + atg[N]) % DIVISOR)
    return


if __name__ == '__main__':
    main()
