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
    [A, B, K] = string_to_int(inputs[0])
    ret = set()
    count = 0
    for v in range(A, B+1):
        if count >= K:
            break
        ret.add(v)
        count += 1
    count = 0
    for v in reversed(range(A, B+1)):
        if count >= K:
            break
        ret.add(v)
        count += 1
    return sorted(list(ret))


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    for r in ret:
        print(r)
