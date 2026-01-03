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
    N = int(inputs[0])
    sq = int(math.sqrt(N)) + 1
    min_s = None
    for n in range(1, sq + 1):
        if N % n == 0:
            m = N // n
            len_m = len(str(m))
            if min_s is None or min_s > len_m:
                min_s = len_m
    return min_s


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
