import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, K] = string_to_int(inputs[0])
    A = string_to_int(inputs[1])
    counter = collections.Counter(A)
    i = len(counter)
    values = counter.most_common()
    change_num = 0
    while i > K:
        change_num += (values[i-1][1])
        i -= 1
    return change_num


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
