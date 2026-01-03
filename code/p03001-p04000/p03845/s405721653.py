import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(T, PX):
    T = string_to_int(T)
    DRINKS = list(map(string_to_int, PX))
    sum_t = reduce(lambda acc, x: acc+x, T, 0)

    ret = []
    for d in DRINKS:
        i = d[0] - 1
        x = d[1]
        ret.append(sum_t - (T[i] - x))
    return ret


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    T = input()
    M = int(input())
    ret = solve(T, inputs(M))
    for r in ret:
        print(r)
