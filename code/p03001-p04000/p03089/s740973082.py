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


def get_list_of_int():
    return [int(i) for i in input().split()]


def get_list_of_float():
    return [float(f) for f in input().split()]


def get_list_of_char():
    return list(input().strip())


def get_data(n, order=None, **kwargs):
    if not order:
        order = range(len(kwargs))
    it = iter(order)
    var, fn = zip(*sorted(sorted(kwargs.items()), key=lambda _: next(it)))

    rows = []
    for _ in range(n):
        rows.append(input().split())
    columns = zip(*rows)
    exec("global "+", ".join(var)+"\n"+"\n".join(
        v+"=list(map(fn[{}], data[{}]))".format(i, i)
        for i, v in enumerate(var)),
        globals(),
        {"fn": list(fn), "data": list(columns)}
    )
    return


# inputs
N = 0
B = []


def set_inputs():
    global N, B
    N = get_int()
    B = get_list_of_int()
    return


# n: int, b: List[int]
def solve(b):
    if len(b) == 0:
        return []
    if sum(b) > len(b) * (len(b) + 1) // 2:
        return [-1]
    for i, v in enumerate(b):
        if v > i + 1:
            return [-1]
    possible_indices = []
    for i, v in enumerate(b):
        if i + 1 == v:
            possible_indices.append(i)
    if len(possible_indices) == 0:
        return [-1]
    for i in possible_indices:
        ans = solve(b[:i] + b[i+1:])
        if len(ans) == 1 and ans[0] == -1:
            continue
        return ans + [i+1]
    return [-1]


def main():
    setrecursionlimit(100000)
    set_inputs()
    for i in solve(B):
        print(i)
    return


if __name__ == '__main__':
    main()
