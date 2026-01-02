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
    A = string_to_int(inputs[0])
    order = {x: i for i, x in enumerate(A)}
    r = []
    for i in range(len(A)):
        r.append(order[i+1]+1)
    return r


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    for i, r in enumerate(ret):
        if i == len(ret) - 1:
            print(r)
        else:
            print('{} '.format(r), end='')
