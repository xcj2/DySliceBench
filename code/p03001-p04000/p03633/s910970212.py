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


def euqrid(a, b):
    if a > b:
        large = a
        small = b
    else:
        large = b
        small = a

    if small == 0:
        return large
    return euqrid(small, large % small)


def calc_m(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        a = numbers.pop()
        b = numbers.pop()
        e = euqrid(a, b)
        return a * b // e
    a = numbers.pop()
    b = calc_m(numbers)
    e = euqrid(a, b)
    return a * b // e


def solve(inputs):
    clocks = inputs
    return calc_m(clocks)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(int_inputs(N))
    print(ret)
