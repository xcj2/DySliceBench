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
    n, m = get_int_list()
    xs = get_int_list()

    if n >= m:
        print(0)
        return
    xs.sort()
    diffs = [a - b for a, b in zip(xs[1:], xs)]
    diffs.sort()
    print(sum(diffs[:m-n]))


if __name__ == '__main__':
    main()
