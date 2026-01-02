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
S = ""


def set_inputs():
    global S
    S = get_str()


def main():
    set_inputs()
    stack = []
    ret = 0
    for c in S:
        if stack and stack[-1] != c:
            ret += 2
            stack.pop(-1)
        else:
            stack.append(c)
    print(ret)


if __name__ == '__main__':
    main()
