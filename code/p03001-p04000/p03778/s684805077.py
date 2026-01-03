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
    [W, a_left, b_left] = string_to_int(inputs[0])
    a_right = a_left + W
    b_right = b_left + W

    if a_right < b_left:
        return b_left - a_right
    elif a_left > b_right:
        return a_left - b_right
    return 0


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
