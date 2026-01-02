import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    [X, Y, Z] = string_to_int(inputs[0])

    i = 0
    max_num = 0
    while (Y + Z) * i <= X:
        used = (Y + Z) * i + Z
        if X >= used:
            max_num = i
        i += 1
    return max_num


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
