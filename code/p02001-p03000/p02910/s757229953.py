import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    for i, c in enumerate(S):
        i += 1
        if i % 2 == 0:
            if c == 'R':
                return 'No'
        else:
            if c == 'L':
                return 'No'
    return 'Yes'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
