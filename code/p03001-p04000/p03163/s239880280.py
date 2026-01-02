from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor

import heapq
import itertools
import operator


inf = float('inf')


def get_int():
    return int(input())


def get_str():
    return input().strip()


def get_list_of_int():
    return [int(i) for i in input().split()]


def get_char_list():
    return list(input().strip())


# inputs
N, W = 0, 0
Ws, Vs = [0], [0]


def set_inputs():
    global N, W, Ws, Vs
    N, W = get_list_of_int()
    ws, vs = [], []
    for _ in range(N):
        w, v = get_list_of_int()
        ws.append(w)
        vs.append(v)
    Ws, Vs = ws, vs


def main():
    set_inputs()
    values = [0] * (W + 1)
    items = [0] * (W + 1)
    for w in range(1, W + 1):
        values[w], items[w] = max((values[w - Ws[i]] + Vs[i], items[w - Ws[i]] | 1 << i) if w - Ws[i] >= 0 and (items[w - Ws[i]] & 1 << i) == 0 else (values[w-1], items[w-1]) for i in range(N))
    print(values[W])


if __name__ == '__main__':
    main()
