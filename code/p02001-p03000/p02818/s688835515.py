import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools
import heapq


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(input):
    [takahashi, aoki, count] = string_to_int(input)

    if count > takahashi:
        count -= takahashi
        takahashi = 0
    else:
        takahashi -= count
        count = 0
        return "{} {}".format(takahashi, aoki)

    if count > aoki:
        return "0 0"
    else:
        aoki -= count
        return "{} {}".format(takahashi, aoki)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(input())
    print(ret)
