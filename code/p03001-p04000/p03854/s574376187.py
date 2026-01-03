import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    target = S
    while len(target) > 0:
        n = len(target)
        candidate1 = target[n-5:]
        candidate2 = target[n-6:]
        candidate3 = target[n-7:]
        if candidate1 == 'dream' or candidate1 == 'erase':
            target = target[:n-5]
        elif candidate2 == 'eraser':
            target = target[:n-6]
        elif candidate3 == 'dreamer':
            target = target[:n-7]
        else:
            return 'NO'
    return 'YES'


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
