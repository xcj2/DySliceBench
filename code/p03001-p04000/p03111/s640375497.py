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
N, A, B, C = 0, 0, 0, 0
L = []


def set_inputs():
    global N, A, B, C, L
    N, A, B, C = get_li()
    L = get_data(N, [int])
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    ans = inf
    for x in itertools.product(range(4), repeat=N):
        take = [[], [], [], []]
        for i in range(N):
            take[x[i]].append(L[i])
        if len(take[0]) == 0 or len(take[1]) == 0 or len(take[2]) == 0:
            continue
        cost = 0
        cost += abs(sum(take[0]) - A)
        cost += abs(sum(take[1]) - B)
        cost += abs(sum(take[2]) - C)
        cost += (len(take[0]) - 1) * 10
        cost += (len(take[1]) - 1) * 10
        cost += (len(take[2]) - 1) * 10
        ans = min(ans, cost)
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
