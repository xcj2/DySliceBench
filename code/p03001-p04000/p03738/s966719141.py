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
    A = inputs[0]
    B = inputs[1]
    if A == B:
        return 'EQUAL'
    if A > B:
        return 'GREATER'
    return 'LESS'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(int_inputs(2))
    print(ret)
