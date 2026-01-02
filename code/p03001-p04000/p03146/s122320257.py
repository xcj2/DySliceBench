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


def f(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def main():
    s = get_int()
    a_set = {s}
    a = f(s)
    for i in itertools.count(2):
        if a in a_set:
            print(i)
            return
        a_set.add(a)
        a = f(a)


if __name__ == '__main__':
    main()
