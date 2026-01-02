import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, X, inputs):
    requires = list(map(lambda x: int(x), inputs))
    count = 0
    for r in requires:
        X -= r
        count += 1
    min_r = min(requires)

    while X >= min_r:
        X -= min_r
        count += 1
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, X] = string_to_int(input())
    ret = solve(N, X, inputs(N))
    print(ret)
