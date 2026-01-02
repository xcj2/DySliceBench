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
A, B, C = [0], [0], [0]


def set_inputs():
    global N, A, B, C
    N = get_int()
    a, b, c = [], [], []
    for _ in range(N):
        x, y, z = get_list_of_int()
        a.append(x)
        b.append(y)
        c.append(z)
    A, B, C = a, b, c


def main():
    set_inputs()
    happiness = [(A[0], B[0], C[0])]
    for i in range(1, N):
        h = happiness[i-1]
        a = max(h[1], h[2]) + A[i]
        b = max(h[0], h[2]) + B[i]
        c = max(h[0], h[1]) + C[i]
        happiness.append((a, b, c))
    print(max(happiness[N-1]))


if __name__ == '__main__':
    main()
