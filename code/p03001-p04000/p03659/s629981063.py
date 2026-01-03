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
    deck = string_to_int(inputs[0])
    sums = []
    for i, card in enumerate(deck):
        if i == 0:
            sums.append(card)
        else:
            sums.append(sums[i-1] + card)

    min_diff = None
    for i, s in enumerate(sums):
        if i == len(sums) - 1:
            break
        arai = sums[-1] - s
        sunuke = s

        if min_diff is None or min_diff > abs(arai - sunuke):
            min_diff = abs(arai - sunuke)
    return min_diff


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
