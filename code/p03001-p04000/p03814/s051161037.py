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
    S = list(inputs[0])
    N = len(S)
    start = None
    for i in range(N):
        if S[i] == 'A':
            start = i
            break
    end = None
    for i in reversed(range(N)):
        if S[i] == 'Z':
            end = i
            break
    return end - start + 1


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
