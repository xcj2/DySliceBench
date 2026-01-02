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
    cities = []
    for _ in range(3):
        cities.extend(get_int_list())

    counter = Counter()
    for c in cities:
        counter[c] += 1
    c2 = Counter()
    for v in counter.values():
        c2[v] += 1
    if list(c2.values()) == [2, 2]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
