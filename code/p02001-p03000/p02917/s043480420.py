import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    B = string_to_int(inputs[0])
    A = []

    candidate = -1
    for i, b in enumerate(B):
        if i == 0:
            A.append(b)
        else:
            if b > candidate:
                A.append(candidate)
            else:
                A.append(b)
        candidate = b
    A.append(b)
    return sum(A)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
