import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools
import heapq


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(input):
    nums = string_to_int(input)

    def euclid(large, small):
        if small == 0:
            return large
        l = large % small
        return euclid(small, l)

    nums.sort(reverse=True)
    eee = euclid(nums[0], nums[1])
    return int((nums[0] * nums[1]) / eee)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(input())
    print(ret)
