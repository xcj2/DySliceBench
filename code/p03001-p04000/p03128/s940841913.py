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


def get_str():
    return input().strip()


def get_int_list():
    return [int(i) for i in input().split()]


def get_char_list():
    return list(input().strip())


COST = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}


# inputs
N, M = 0, 0
A = [0]


def hoge():
    d = dict()
    def labeler(label, iter):
        enumerate()


def set_inputs():
    global N, M, A
    N, M = get_int_list()
    A = get_int_list()


@lru_cache(maxsize=None)
def dp(i):
    if i < 0:
        return -inf
    elif i == 0:
        return 0
    return max(dp(i - COST[a]) + 1 for a in A)


def main():
    setrecursionlimit(100000)
    set_inputs()

    candidates = sorted(A, reverse=True)
    ret = []
    n = N
    for i in range(dp(N)):
        for a in candidates:
            cond = True
            if i == dp(N) - 1:
                cond = COST[a] == n
            if dp(n - COST[a]) == dp(n) - 1 and cond:
                ret.append(a)
                n -= COST[a]
                break
    print(''.join(str(r) for r in ret))


if __name__ == '__main__':
    main()
