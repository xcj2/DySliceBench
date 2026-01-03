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
    [s_num, c_num] = string_to_int(inputs[0])

    scc_num = 0

    if s_num * 2 <= c_num:
        scc_num += s_num
        c_num -= (s_num * 2)
        scc_num += c_num // 4
    else:
        scc_num += c_num // 2
        c_num -= c_num // 2
        # scc_num += c_num // 4
    return scc_num


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
