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


def split_goals_by_m(goals, m):
    ret = []
    tmp = []
    for g in goals:
        if g == m:
            if tmp:
                ret.append(tmp)
                tmp = []
        else:
            tmp.append(g - m)
    if tmp:
        ret.append(tmp)
    return ret


def get_ans(goals):
    m = min(goals)
    gs = split_goals_by_m(goals, m)
    if len(gs) == 0:
        return m
    ret = m
    for g in gs:
        ret += get_ans(g)
    return ret


def main():
    n = get_int()
    hs = get_int_list()

    print(get_ans(hs))


if __name__ == '__main__':
    main()
