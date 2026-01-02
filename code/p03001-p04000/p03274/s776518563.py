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
N, K = 0, 0
X = []


def set_inputs():
    global N, K, X
    N, K = get_li()
    X = get_li()
    return


def twice(x):
    return x[0] * 2, x[1]


def find_index(l, x):
    if x in l:
        return l.index(x)
    return inf


def main():
    setrecursionlimit(100000)
    set_inputs()
    ans = inf
    for i in range(N-K+1):
        l, r = X[i], X[i+K-1]
        tmp = min(abs(l) + abs(l-r), abs(r) + abs(r-l))
        ans = min(ans, tmp)
    print(ans)
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
