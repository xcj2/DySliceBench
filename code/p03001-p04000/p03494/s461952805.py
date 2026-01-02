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
    A = string_to_int(inputs[0])
    min_devide_num = -1
    for a in A:
        count = 0
        while a % 2 == 0:
            a /= 2
            count += 1
        if min_devide_num == -1 or min_devide_num > count:
            min_devide_num = count
    return min_devide_num


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
