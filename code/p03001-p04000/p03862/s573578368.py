import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, X] = string_to_int(inputs[0])
    A = string_to_int(inputs[1])

    count = 0
    for i in range(N-1):
        if A[i] > X:
            count += abs(X - A[i])
            A[i] = X
        if A[i] + A[i+1] >= X:
            count += abs(X - (A[i+1] + A[i]))
            A[i+1] = X - A[i]
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
