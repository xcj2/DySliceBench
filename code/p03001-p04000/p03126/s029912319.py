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
    kas = []
    for _ in range(n):
        kas.append(get_int_list())

    counter = Counter()
    for ka in kas:
        for x in ka[1:]:
            counter[x] += 1
    print(len(list(filter(lambda x: x == n, counter.values()))))


if __name__ == '__main__':
    main()
