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
N, M = 0, 0
P, Y = [], []


def set_inputs():
    global N, M, P, Y
    N, M = get_li()
    P, Y = get_data(M, [int, int])
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    prefecture = defaultdict(list)
    lst = [""] * M
    for i, (p, y) in enumerate(zip(P, Y)):
        prefecture[p].append((i, y))
    for k in prefecture.keys():
        prefecture[k].sort(key=operator.itemgetter(1))
        for i, (n, y) in enumerate(prefecture[k]):
            lst[n] = "{:06d}{:06d}".format(k, i + 1)
    for v in lst:
        print(v)
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
