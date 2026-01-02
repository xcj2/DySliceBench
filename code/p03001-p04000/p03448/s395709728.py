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
    A500 = int(inputs[0])
    B100 = int(inputs[1])
    C50 = int(inputs[2])
    X = int(inputs[3])

    count = 0
    for a in range(A500 + 1):
        for b in range(B100 + 1):
            for c in range(C50 + 1):
                m = a * 500 + b * 100 + c * 50
                if m == X:
                    count += 1
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(4))
    print(ret)
