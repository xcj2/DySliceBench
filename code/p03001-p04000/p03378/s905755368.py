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
    [N, M, X] = string_to_int(inputs[0])
    A = string_to_int(inputs[1])
    cost_0 = 0
    cost_n = 0
    for a in A:
        if a < X:
            cost_0 += 1
        elif a > X:
            cost_n += 1
    return min([cost_0, cost_n])


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
