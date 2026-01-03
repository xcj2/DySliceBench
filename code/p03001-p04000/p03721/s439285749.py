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
    values = list(map(string_to_int, inputs))
    values.sort(key=lambda x: x[0])
    count = 0
    for v in values:
        count += v[1]
        if count >= K:
            return v[0]


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, K] = string_to_int(input())
    ret = solve(N, K, inputs(N))
    print(ret)
