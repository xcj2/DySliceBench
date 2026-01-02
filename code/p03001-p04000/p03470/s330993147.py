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
    mochis = list(map(int, inputs))
    mochis.sort(reverse=True)
    count = 0
    prev_mochi = -1
    for m in mochis:
        if prev_mochi == -1 or prev_mochi > m:
            count += 1
        prev_mochi = m
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
