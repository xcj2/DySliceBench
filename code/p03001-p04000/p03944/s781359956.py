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


def solve(W, H, N, inputs):
    actions = list(map(string_to_int, inputs))
    white_x1 = 0
    white_x2 = W
    white_y1 = 0
    white_y2 = H

    for a in actions:
        if a[2] == 1:
            if white_x1 < a[0]:
                white_x1 = a[0]
        elif a[2] == 2:
            if white_x2 > a[0]:
                white_x2 = a[0]
        elif a[2] == 3:
            if white_y1 < a[1]:
                white_y1 = a[1]
        elif a[2] == 4:
            if white_y2 > a[1]:
                white_y2 = a[1]

    if white_x1 >= white_x2 or white_y1 >= white_y2:
        return 0
    return (white_x2 - white_x1) * (white_y2 - white_y1)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [W, H, N] = string_to_int(input())
    ret = solve(W, H, N, inputs(N))
    print(ret)
