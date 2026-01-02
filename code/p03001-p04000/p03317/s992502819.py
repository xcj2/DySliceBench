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
    [N, K] = string_to_int(inputs[0])
    paint_range = K-1
    A = string_to_int(inputs[1])
    one_index = None

    for i, a in enumerate(A):
        one_index = i if a == 1 else one_index
    count = one_index // paint_range
    r = one_index % paint_range
    over = 0
    if r != 0:
        count += 1
        over = paint_range - r
    count += math.ceil(((N-1) - one_index - over) / paint_range)
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
