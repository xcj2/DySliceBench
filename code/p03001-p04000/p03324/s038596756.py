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
    [D, n] = string_to_int(inputs[0])
    N = n + 1 if n == 100 else n
    adder = reduce(lambda acc, _: acc * 100, range(D), 1)
    count = 0
    for _ in range(N):
        count += adder
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
