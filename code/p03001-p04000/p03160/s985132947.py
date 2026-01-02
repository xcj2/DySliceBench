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
N = 0
H = [0]


def set_inputs():
    global N, H
    N = get_int()
    H = get_list_of_int()


def main():
    set_inputs()
    cost = [inf] * N
    cost[0] = 0
    cost[1] = abs(H[0] - H[1])
    for i in range(2, N):
        cost[i] = min(
            cost[i-1] + abs(H[i] - H[i-1]),
            cost[i-2] + abs(H[i] - H[i-2])
        )
    print(cost[N-1])


if __name__ == '__main__':
    main()
