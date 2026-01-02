from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor
from sys import setrecursionlimit

import heapq
import itertools
import operator
import re


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
N, Q = 0, 0
S = ""
L, R = [], []


def set_inputs():
    global N, Q, S, L, R
    N, Q = get_li()
    S = get_str()
    L, R = get_data(Q, [int, int])
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    a, c = [], []
    for m in re.finditer("AC", S):
        a.append(m.start())
        c.append(m.end())
    for l, r in zip(L, R):
        s = bisect_left(a, l-1)
        e = bisect_right(c, r)
        if e - s <= 0:
            print(0)
        else:
            print(e - s)
    return


# ACACACXACXXAC
# a = [0, 2, 4, 7, 11]
# c = [2, 4, 6, 9, 13]


if __name__ == '__main__':
    main()
