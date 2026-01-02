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
    [D, X] = string_to_int(inputs[0])
    A = list(map(int, inputs[1:]))

    choco = X
    for a in A:
        d = 0
        while d * a + 1 <= D:
            choco += 1
            d += 1

    return choco


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N+1))
    print(ret)
