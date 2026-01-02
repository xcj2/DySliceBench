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
    s = inputs[0]
    t = inputs[1]
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort(reverse=True)
    s_ret = ''.join(s_list)
    t_ret = ''.join(t_list)

    return 'Yes' if s_ret < t_ret else 'No'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
