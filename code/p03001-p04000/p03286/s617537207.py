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


def set_inputs():
    global N
    N = get_int()
    return


def base_10_to_n(x, n):
    mod = x % n
    mod = abs(mod)
    div = (x - mod) // n
    if div == 0:
        return str(mod)
    return base_10_to_n(div, n) + str(mod)


def main():
    setrecursionlimit(100000)
    set_inputs()
    print(base_10_to_n(N, -2))
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
