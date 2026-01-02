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
    numbers = inputs
    number_set = set()

    for n in numbers:
        if n in number_set:
            number_set.remove(n)
        else:
            number_set.add(n)
    return len(number_set)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(int_inputs(N))
    print(ret)
