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
    roads = list(map(string_to_int, inputs))
    towns = {i+1: [] for i in range(N)}

    for r in roads:
        towns[r[0]].append(r[1])
        towns[r[1]].append(r[0])
    ret = []

    for t in sorted(towns.keys()):
        ret.append(len(towns[t]))
    return ret


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    for r in ret:
        print(r)
