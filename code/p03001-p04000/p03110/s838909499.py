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


def get_list_of_float():
    return [float(i) for i in input().split()]


def get_char_list():
    return list(input().strip())


YPB = 380000.0


# inputs
N = 0
X = [0.0]
U = [""]


def set_inputs():
    global N, X, U
    N = get_int()
    X = []
    U = []
    for _ in range(N):
        x, u = get_str().split()
        X.append(float(x))
        U.append(u)


def main():
    set_inputs()
    sum = 0.0
    for i in range(N):
        u = 1
        if U[i] == 'BTC':
            u = YPB
        sum += X[i] * u
    print(sum)


if __name__ == '__main__':
    main()
