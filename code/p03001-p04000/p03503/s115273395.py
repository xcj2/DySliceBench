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
    N = len(inputs) // 2
    stores_hour = list(map(string_to_int, inputs[:N]))
    benefit_table = list(map(string_to_int, inputs[N:]))

    pattern_num = 2 ** 10

    max_benefit = None
    for i in range(1, pattern_num):
        bits = bin(i)[2:]
        less_digit = 10 - len(bits)
        zero_padding = ['0' for i in range(less_digit)]
        pattern = zero_padding + list(bits)

        benefit = 0
        for i, store in enumerate(stores_hour):
            match_count = 0
            for j, t in enumerate(store):
                if int(pattern[j]) == 1 and t == 1:
                    match_count += 1
            benefit += benefit_table[i][match_count]
        if max_benefit is None or max_benefit < benefit:
            max_benefit = benefit
    return max_benefit


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N * 2))
    print(ret)
