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


def solve(H, W, inputs):
    S = inputs
    for _ in range(W+2):
        print('#', end='')
    print('')

    for s in S:
        print('#', end='')
        print(s, end='')
        print('#')

    for _ in range(W+2):
        print('#', end='')
    print('')


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [H, W] = string_to_int(input())
    ret = solve(H, W, inputs(H))
    # print(ret)
