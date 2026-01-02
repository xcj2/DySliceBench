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
    hps = get_int_list()

    x = min(hps)
    while True:
        mod = [v % x for v in hps]
        mod = list(filter(lambda x: x > 0, mod))
        if mod and min(mod) < x:
            x = min(mod)
        else:
            print(x)
            return


if __name__ == '__main__':
    main()
