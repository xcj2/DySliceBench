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


def is_match(parent, child, pi, pj):
    for ci in range(len(child)):
        for cj in range(len(child[ci])):
            # c = child[ci][cj]
            # p = parent[pi+ci][pj+cj]
            if child[ci][cj] != parent[pi+ci][pj+cj]:
                return False
    return True


def solve(N, M, inputs):
    map_parent = list(map(list, inputs[:N]))
    map_child = list(map(list, inputs[N:]))

    for pi in range(0, N-M+1):
        for pj in range(0, N-M+1):
            if is_match(map_parent, map_child, pi, pj):
                return 'Yes'
    return 'No'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(N+M))
    print(ret)