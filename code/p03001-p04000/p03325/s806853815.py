import sys
from collections import deque
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    A = string_to_int(inputs[0])
    odds = []

    for a in A:
        if a % 2 == 0:
            odds.append(a)
    count = 0
    for o in odds:
        while o % 2 != 1:
            o /= 2
            count += 1

    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
