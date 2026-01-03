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
    A = string_to_int(inputs[0])
    b = collections.deque([])

    for i, a in enumerate(A):
        if i % 2 == 0:
            b.append(str(a))
        else:
            b.appendleft(str(a))
    if len(b) % 2 != 0:
        b.reverse()
    return ' '.join(b)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)