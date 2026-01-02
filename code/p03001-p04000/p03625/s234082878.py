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
    rods = string_to_int(inputs[0])
    rods_counter = collections.Counter(rods)
    available_rods = []
    four_count_rods = []
    for length, count in rods_counter.items():
        if count >= 2:
            available_rods.append(length)
        if count >= 4:
            four_count_rods.append(length)
    available_rods.sort()
    four_count_rods.sort()

    max_square = []

    if len(available_rods) < 2:
        max_square.append(0)
    else:
        max_square.append(available_rods[-1] * available_rods[-2])

    if len(four_count_rods) < 1:
        max_square.append(0)
    else:
        max_square.append(four_count_rods[-1] * four_count_rods[-1])
    return max(max_square)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
