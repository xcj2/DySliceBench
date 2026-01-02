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
V = []


def set_inputs():
    global N, V
    N = get_int()
    V = get_li()
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    x = V[0::2]
    y = V[1::2]
    x_counter = Counter(x)
    y_counter = Counter(y)
    x_val, x_cnt = x_counter.most_common(1)[0]
    y_val, y_cnt = y_counter.most_common(1)[0]
    ans = N - x_cnt - y_cnt
    if x_val == y_val:
        if len(x_counter) == 1:
            if len(y_counter) == 1:
                ans = N // 2
            else:
                _, y_cnt = y_counter.most_common(2)[1]
                ans = N - x_cnt - y_cnt
        else:
            if len(y_counter) == 1:
                _, x_cnt = x_counter.most_common(2)[1]
                ans = N - x_cnt - y_cnt
            else:
                _, x_cnt_2 = x_counter.most_common(2)[1]
                _, y_cnt_2 = y_counter.most_common(2)[1]
                ans = min(N - x_cnt - y_cnt_2, N - x_cnt_2 - y_cnt)
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
