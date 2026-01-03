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
    A = string_to_int(inputs[0])
    n = len(A)
    count4 = 0
    count2 = 0
    for a in A:
        if a % 4 == 0:
            count4 += 1
        elif a % 2 == 0:
            count2 += 1
    count2 = count2 // 2
    requirements = n // 2

    if requirements <= count4 + count2:
        return 'Yes'
    return 'No'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)

