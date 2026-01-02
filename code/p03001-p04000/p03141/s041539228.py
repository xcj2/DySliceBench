from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor

import heapq
import itertools
import operator


def get_int():
    return int(input())


def get_str():
    return input().strip()


def get_int_list():
    return [int(i) for i in input().split()]


def get_char_list():
    return list(input().strip())


def main():
    n = get_int()
    A = []
    B = []
    for _ in range(n):
        a, b = get_int_list()
        A.append(a)
        B.append(b)

    sums = [(i, a + b) for i, (a, b) in enumerate(zip(A, B))]
    sums.sort(key=lambda x: x[1], reverse=True)
    takahashi = [A[i] for i, _ in sums[0::2]]
    aoki = [B[i] for i, _ in sums[1::2]]
    print(sum(takahashi) - sum(aoki))


if __name__ == '__main__':
    main()
