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
    O = list(inputs[0])
    E = list(inputs[1])
    O.reverse()
    E.reverse()

    s = []
    for i in range(len(E)):
        s.append(O.pop())
        s.append(E.pop())
    if len(O) != 0:
        s.append(O.pop())
    return ''.join(s)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
