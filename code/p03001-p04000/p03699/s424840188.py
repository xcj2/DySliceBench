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
    S = inputs
    S.sort()
    total = reduce(lambda acc, x: acc+x, S, 0)
    if total % 10 == 0:
        for s in S:
            if s % 10 != 0:
                total -= s
                break
    return 0 if total % 10 == 0 else total


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(int_inputs(N))
    print(ret)
