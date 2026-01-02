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
    routes = list(map(string_to_int, inputs))
    current = [0, 0]
    t = 0
    for r in routes:
        diff_t = r[0] - t
        diff = abs(r[1] - current[0]) + abs(r[2] - current[1])

        if diff_t >= diff and (diff_t % 2) == (diff % 2):
            current = [r[1], r[2]]
            t = r[0]
        else:
            return 'No'
    return 'Yes'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
