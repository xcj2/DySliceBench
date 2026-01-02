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
    nums = string_to_int(inputs[0])
    max_num = max(nums)
    sum_num = sum(nums)

    count = 0
    while sum_num % 3 != 0 or (sum_num // 3) < max_num:
        count += 1
        sum_num += 2
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
