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
    chains_list = list(map(string_to_int, inputs))
    chains = {i+1: set() for i in range(N)}
    for c in chains_list:
        chains[c[0]].add(c[1])
        chains[c[1]].add(c[0])

    if 1 not in chains:
        return "IMPOSSIBLE"
    hops = chains[1]

    for h in hops:
        if N in chains[h]:
            return "POSSIBLE"
    return "IMPOSSIBLE"


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)
