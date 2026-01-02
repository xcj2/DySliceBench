import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    X = int(inputs[0])
    max = 1
    for x in range(1, X + 1):
        for y in range(2, X + 1):
            c = x ** y
            if c <= X:
                max = c if c > max else max
            else:
                break
    return max


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
