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
    A = string_to_int(inputs[0])
    rate = [399, 799, 1199, 1599, 1999, 2399, 2799, 3199]
    rate_num = len(rate)

    counter_overs = 0
    rate_set = set()
    for a in A:
        if a >= 3200:
            counter_overs += 1
        else:
            hit = None
            for i, r in enumerate(reversed(rate)):
                if a <= r:
                    hit = i
            rate_set.add(hit)
    if len(rate_set) == 0:
        # max_num = counter_overs if counter_overs <= rate_num else rate_num
        max_num = counter_overs
        min_num = 1
    else:
        sum_all = len(rate_set) + counter_overs
        # max_num = sum_all if sum_all <= rate_num else rate_num
        max_num = sum_all
        min_num = len(rate_set)
    return "{} {}".format(min_num, max_num)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
