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
D, G = 0, 0
P, C = [], []


def set_inputs():
    global D, G, P, C
    D, G = get_li()
    P, C = get_data(D, [int, int])
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    all_d = set(range(1, D+1))
    ans = inf
    for i in range(2 ** D):
        comp_d = {j + 1 for j in range(D) if ((1 << j) & i) != 0}
        p = sum(100 * d * P[d-1] + C[d-1] for d in comp_d)
        s = sum(P[d-1] for d in comp_d)
        additional_p = 0
        available_p = 0
        if p < G and i != 2 ** D - 1:
            max_other_d = max(all_d - comp_d)
            additional_p = 100 * max_other_d
            available_p = additional_p * (P[max_other_d-1] - 1)
        if p + available_p < G:
            continue
        tmp = s
        if additional_p:
            tmp += (G - p + additional_p - 1) // additional_p
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
