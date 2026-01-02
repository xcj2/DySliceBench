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


def get_root(root, x):
    y = x
    while y != root.get(y, y):
        y = root.get(y, y)
    z = x
    while z != root.get(z, z):
        root[z] = y
        z = root.get(z, z)
    return y


# inputs
N, M = 0, 0
A, B = [], []


def set_inputs():
    global N, M, A, B
    N, M = get_list_of_int()
    for _ in range(M):
        a, b = get_list_of_int()
        A.append(a)
        B.append(b)


def main():
    set_inputs()
    nc2 = N * (N - 1) // 2
    inconv = [0] * M
    conns = 0
    root = dict()
    conns_dict = defaultdict(int)
    for i in range(1, M+1):
        inconv[M-i] = nc2 - conns
        if i == M:
            break
        a, b = A[M-i], B[M-i]
        a_root = get_root(root, a)
        a_conns = conns_dict[a_root]
        b_root = get_root(root, b)
        b_conns = conns_dict[b_root]
        if a_conns == 0 and b_conns == 0:
            root[a] = a
            root[b] = a
            conns_dict[a] = 2
            conns += 1
        elif a_conns == 0:
            root[a] = b_root
            conns_dict[b_root] = b_conns + 1
            conns += b_conns
        elif b_conns == 0:
            root[b] = a_root
            conns_dict[a_root] = a_conns + 1
            conns += a_conns
        elif a_root != b_root:
            root[b_root] = a_root
            conns_dict[a_root] = a_conns + b_conns
            conns += a_conns * b_conns
    for i in inconv:
        print(i)


if __name__ == '__main__':
    main()
