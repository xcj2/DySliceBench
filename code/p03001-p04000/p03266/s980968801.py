from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, factorial, floor
from sys import setrecursionlimit

import heapq
import itertools
import operator


inf = float('inf')


# globals
N, K = 0, 0


def set_inputs():
    global N, K
    N, K = get_li()
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    sum_abc = itertools.dropwhile(
        lambda x: x < 3,
        itertools.takewhile(
            lambda x: x <= 3 * N,
            itertools.count(2 * K, K)
        )
    )
    ans = 0
    if K % 2 == 0:
        # a + b + c = (l + m + n) * (K // 2)
        # a, b, c >= 1
        x = N // K
        y = N // (K // 2) - x
        ans = x ** 3 + y ** 3
    else:
        # 2 * (a + b + c) = (l + m + n) * K
        x = N // K
        ans = x ** 3
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
