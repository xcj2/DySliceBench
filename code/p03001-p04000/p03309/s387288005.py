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
A = []
X = []


def set_inputs():
    global N, A
    N = get_int()
    A = get_li()
    return


def f(n):
    return sum(abs(x-n) for x in X)


def main():
    global X
    setrecursionlimit(100000)
    set_inputs()
    X = [a - (i + 1) for i, a in enumerate(A)]
    X.sort()
    b = X[0]
    i = 1
    passed = 0
    same = 1
    coming = N - 1
    ans = f(b)
    tmp = ans
    while i < N:
        if X[i] == b:
            same += 1
            coming -= 1
            i += 1
            continue
        diff = X[i] - b
        tmp = tmp + (passed + same - coming) * diff
        ans = min(ans, tmp)
        b = X[i]
        passed += same
        same = 1
        coming -= 1
        i += 1
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
