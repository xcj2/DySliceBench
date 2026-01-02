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
    n, a, b = get_int_list()
    max_ = min(a, b)
    min_ = max(0, a + b - n)
    print("{} {}".format(max_, min_))


if __name__ == '__main__':
    main()
