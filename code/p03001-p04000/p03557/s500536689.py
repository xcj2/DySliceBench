import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    A = string_to_int(inputs[1])
    B = string_to_int(inputs[2])
    C = string_to_int(inputs[3])
    A.sort()
    B.sort()
    C.sort()

    patterns = 0

    for b in B:
        ai = bisect.bisect_left(A, b)
        ci = bisect.bisect_right(C, b)
        patterns += ai * (N-ci)

    return patterns


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(4))
    print(ret)
