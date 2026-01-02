import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    A = string_to_int(inputs[0])
    B = string_to_int(inputs[1])
    C = string_to_int(inputs[2])
    s = 0
    prev_i = -1
    for i in A:
        i -= 1
        s += B[i]
        if prev_i != -1 and i == prev_i + 1:
            s += C[prev_i]
        prev_i = i

    return s


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(3))
    print(ret)
