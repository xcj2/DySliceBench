from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
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
    a = get_char_list()
    b = get_char_list()
    c = get_char_list()

    ret = 0
    for x, y, z in zip(a, b, c):
        if x == y == z:
            continue
        elif x == y or x == z or y == z:
            ret += 1
        else:
            ret += 2
    print(ret)


if __name__ == '__main__':
    main()
