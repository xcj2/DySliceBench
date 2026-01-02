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


# globals
N = 0
X, Y, H = [], [], []


def set_inputs():
    global N, X, Y, H
    N = get_int()
    X, Y, H = get_data(N, [int, int, int])
    return


def answer(cx, cy):
    x, y, h = next(itertools.dropwhile(
        lambda v: v[2] == 0,
        zip(X, Y, H)
    ))
    ch = h + abs(x - cx) + abs(y - cy)
    for x, y, h in zip(X, Y, H):
        if max(ch - abs(x - cx) - abs(y - cy), 0) != h:
            return False
    print(cx, cy, ch)
    return True


def main():
    setrecursionlimit(100000)
    set_inputs()
    for cx in range(0, 101):
        for cy in range(0, 101):
            if answer(cx, cy):
                return
    return


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


if __name__ == '__main__':
    main()
