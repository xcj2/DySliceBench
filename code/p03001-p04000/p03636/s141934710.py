import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    s = inputs[0]
    count = 0
    for i, c in enumerate(s):
        if i == 0:
            first = c
        elif i == len(s) - 1:
            last = c
        else:
            count += 1
    return '{}{}{}'.format(first, count, last)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
