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
    A = string_to_int(inputs[0])
    A.sort()
    apper = collections.Counter()

    for a in A:
        apper[a] += 1

    start = 1 if len(A) % 2 == 0 else 0
    for i in range(start, len(A), 2):
        if i not in apper:
            return 0
        if i == 0 and apper[0] != 1:
            return 0
        if i != 0 and apper[i] != 2:
            return 0
    if 0 in apper:
        apper.pop(0)

    return (2 ** len(apper)) % 1000000007


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
