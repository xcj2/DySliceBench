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
N, M, C = 0, 0, 0
B = []
A = []


def set_inputs():
    global N, M, C, B, A
    N, M, C = get_list_of_int()
    B = get_list_of_int()
    for _ in range(N):
        a = get_list_of_int()
        A.append(a)
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    ans = 0
    for i in range(N):
        sum = C
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum > 0:
            ans += 1
    print(ans)
    return


if __name__ == '__main__':
    main()
