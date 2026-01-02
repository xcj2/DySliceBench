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
S, T = "", ""


def set_inputs():
    global S, T
    S = get_str()
    T = get_str()
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    mapper = dict()
    inverser = dict()
    for s, t in zip(S, T):
        m = mapper.get(s, None)
        if m and m != t:
            print("No")
            return
        mapper[s] = t
        i = inverser.get(t, None)
        if i and i != s:
            print("No")
            return
        inverser[t] = s
    print("Yes")
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
