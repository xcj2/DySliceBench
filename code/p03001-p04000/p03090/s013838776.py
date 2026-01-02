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


def set_inputs():
    global N
    N = get_int()
    return


def find(n):
    bits = []
    for i in range(2**(n*(n-1)//2)):
        bits = [(i >> j) % 2 for j in range(n*(n-1)//2)]
        cnt = Counter()
        for j in range(1, n+1):
            cnt[j] = 0
        edges = []
        for x, y in itertools.compress(
                itertools.combinations(range(1, n+1), 2),
                bits
        ):
            cnt[x] += y
            cnt[y] += x
            edges.append((x, y))
        counts = list(cnt.values())
        if len(edges) > 0 and all(v == counts[0] for v in counts):
            print(i, bits, edges)


def solve(n):
    s = n
    if n % 2 == 0:
        s = n + 1
    print(n * (n - 1) // 2 - (n // 2))
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i + j == s:
                continue
            print(i, j)


def main():
    setrecursionlimit(100000)
    set_inputs()
    solve(N)
    return


if __name__ == '__main__':
    main()
