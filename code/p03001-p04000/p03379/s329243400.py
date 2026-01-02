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
    sorted_nums = sorted(nums)
    N = len(nums)
    medians = []
    median_candidate = [sorted_nums[N//2 - 1], sorted_nums[N//2]]
    for a in nums:
        if a <= median_candidate[0]:
            medians.append(median_candidate[1])
        else:
            medians.append(median_candidate[0])
    return medians


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    for r in ret:
        print(r)
