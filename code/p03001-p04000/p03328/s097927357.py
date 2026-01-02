import sys
from collections import deque
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [A, B] = string_to_int(inputs[0])
    trees = [0]
    for i in range(1, 1000):
        trees.append(trees[i-1] + i)

    diff = B - A
    return trees[diff] - B


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
