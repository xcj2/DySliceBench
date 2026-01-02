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


def main():
    setrecursionlimit(100000)
    set_inputs()
    if N == 0:
        print(0)
        return
    n = N
    ans = []
    while n != 0:
        rem = n % 2
        n = (n - rem) // (-2)
        ans.append(rem)
    ans.reverse()
    print("".join(map(str, ans)))
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
