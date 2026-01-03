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
    S = inputs[0]
    for i in range(len(S)-1):
        new_s = S[:len(S) - i - 1]
        if len(new_s) % 2 != 0:
            continue
        half = len(new_s) // 2
        front = new_s[:half]
        tail = new_s[half:]

        if front == tail:
            return len(new_s)
    return 0


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
