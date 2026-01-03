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


def solve(N, K, inputs):
    rods = string_to_int(inputs[0])
    rods.sort()
    length = 0
    for i in range(K):
        length += rods.pop()
    return length


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, K] = string_to_int(input())
    ret = solve(N, K, inputs(1))
    print(ret)
