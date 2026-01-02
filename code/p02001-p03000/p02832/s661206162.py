import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools
import heapq


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(input):
    bricks = string_to_int(input)
    count = 1
    broken = 0
    for b in bricks:
        if b == count:
            count += 1
            continue
        broken += 1

    return -1 if broken == len(bricks) else broken


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(input())
    print(ret)
