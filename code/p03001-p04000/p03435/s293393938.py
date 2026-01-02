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
    grid = list(map(string_to_int, inputs))

    for x in range(101):
        a = [-1, -1, -1]
        b = [-1, -1, -1]
        a[0] = x
        for j in range(3):
            b[j] = grid[0][j] - a[0]
        a[1] = grid[1][0] - b[0]
        a[2] = grid[2][0] - b[0]

        for i in range(3):
            for j in range(3):
                if grid[i][j] != a[i] + b[j]:
                    return 'No'
    return 'Yes'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(3))
    print(ret)
