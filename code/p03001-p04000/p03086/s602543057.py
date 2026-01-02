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


# inputs
S = ""


def set_inputs():
    global S
    S = get_str()
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    ans = 0
    tmp = 0
    for c in S:
        if c in "ACGT":
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp = 0
    print(ans)
    return


if __name__ == '__main__':
    main()
