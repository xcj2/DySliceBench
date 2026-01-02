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
    [A, B, C, x, y] = string_to_int(inputs[0])
    cost = 0
    if A + B > C * 2:
        while x >= 1 and y >= 1:
            cost += C * 2
            x -= 1
            y -= 1

    if A > C * 2:
        while x >= 1:
            cost += C * 2
            x -= 1
    else:
        while x >= 1:
            cost += A
            x -= 1

    if B > C * 2:
        while y >= 1:
            cost += C * 2
            y -= 1
    else:
        while y >= 1:
            cost += B
            y -= 1
    return cost


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
