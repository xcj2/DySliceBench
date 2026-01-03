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
    SSSS = 10 ** 9 + 7
    [A, B] = string_to_int(inputs[0])
    max_len = max([A, B])
    min_len = min([A, B])
    diff_len = abs(A-B)
    if diff_len >= 2:
        return 0

    pattern = 0
    for i in reversed(range(1, min_len + 1)):
        if i == min_len:
            if diff_len == 1:
                pattern = max_len * min_len
                pattern *= min_len
            else:
                pattern = min_len + min_len
                pattern *= min_len
        else:
            pattern *= i * i
        pattern = pattern % SSSS

    return pattern % SSSS


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
