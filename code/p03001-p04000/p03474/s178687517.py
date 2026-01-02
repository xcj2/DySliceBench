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
    [A, B] = string_to_int(inputs[0])
    S = inputs[1]
    code = S.split('-')
    if len(code) != 2 or len(code[0]) != A or len(code[1]) != B:
        return 'No'
    return 'Yes'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
