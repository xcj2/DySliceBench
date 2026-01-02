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
N, M = 0, 0
A, B = [], []


def set_inputs():
    global N, M, A, B
    N, M = get_list_of_int()
    get_data(N, A=int, B=int)
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    AB = sorted(zip(A, B))
    ans = 0
    cnt = 0
    for (a, b) in AB:
        if cnt + b <= M:
            ans += a * b
            cnt += b
            continue
        while cnt < M:
            ans += a
            cnt += 1
        break
    print(ans)
    return


if __name__ == '__main__':
    main()
