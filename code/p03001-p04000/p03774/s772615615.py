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


def solve(N, M, inputs):
    students = list(map(string_to_int, inputs[:N]))
    points = list(map(string_to_int, inputs[N:]))
    s_p = []

    for s in students:
        min_d = None
        min_p = None
        for i, p in enumerate(points):
            d = abs(s[0] - p[0]) + abs(s[1] - p[1])
            if min_d is None or min_d > d:
                min_d = d
                min_p = i
        s_p.append(min_p+1)
    return s_p


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(N+M))
    for r in ret:
        print(r)
