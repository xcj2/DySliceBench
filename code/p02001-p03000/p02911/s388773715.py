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


def solve(N, K, answers):
    min_point = K - len(answers)
    points = [min_point for i in range(N)]
    for a in answers:
        points[a-1] += 1
    return ['Yes' if p > 0 else 'No' for p in points]


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, K, Q] = string_to_int(input())
    ret = solve(N, K, int_inputs(Q))
    for r in ret:
        print(r)
