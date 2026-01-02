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
    value_sum = sum(Vs)
    weights = [inf] * (value_sum + 1)
    items = [0] * (value_sum + 1)
    weights[0] = 0
    for v in range(1, value_sum + 1):
        weights[v], items[v] = min((weights[v - Vs[i]] + Ws[i], items[v - Vs[i]] | 1 << i) if v - Vs[i] >= 0 and (items[v - Vs[i]] & 1 << i) == 0 else (inf, 0) for i in range(N))
    max_value = next(i for i in reversed(range(value_sum + 1)) if weights[i] <= W)
    print(sum(Vs[i] if items[max_value] & 1 << i > 0 else 0 for i in range(N)))


if __name__ == '__main__':
    main()
