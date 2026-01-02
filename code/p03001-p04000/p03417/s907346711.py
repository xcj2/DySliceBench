import sys
from functools import reduce
import copy
import math
from pprint import pprint


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, M] = string_to_int(inputs[0])
    if N == 1 and M == 1:
        return 1
    if N == 1 or M == 1:
        return (N * M) - 2
    # if N == 2 and M == 2:
    #     return 0
    if N == 2 or M == 2:
        return 0

    return (N*M) - (N * 2 + M * 2 - 4)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
