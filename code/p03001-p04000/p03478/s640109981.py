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
    [N, A, B] = string_to_int(inputs[0])

    total_sum = 0
    for i in range(1, N+1):
        sum_num = reduce(lambda acc, x: acc + int(x), str(i), 0)
        if sum_num >= A and sum_num <= B:
            total_sum += i
    return total_sum


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
