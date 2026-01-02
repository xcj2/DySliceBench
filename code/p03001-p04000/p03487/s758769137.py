import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    A = string_to_int(inputs[0])
    counter = collections.Counter()
    del_num = 0
    LIMIT = 10 ** 5 + 1
    for a in A:
        if a >= LIMIT:
            del_num += 1
        else:
            counter[a] += 1
    for k in counter.keys():
        c = counter[k]
        if k > c:
            del_num += c
        else:
            del_num += c - k
    return del_num


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
