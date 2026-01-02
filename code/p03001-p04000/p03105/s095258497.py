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
A, B, C = 0, 0, 0


def set_inputs():
    global A, B, C
    A, B, C = get_list_of_int()


def main():
    set_inputs()
    print(min(C, B // A))


if __name__ == '__main__':
    main()
