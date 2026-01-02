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
    [N, Y] = string_to_int(inputs[0])
    Y = Y // 1000

    for n10 in reversed(range(N+1)):
        for n5 in reversed(range(N - n10 + 1)):
            n1 = N - (n10 + n5)
            if n1 >= 0:
                money = 10 * n10 + 5 * n5 + 1 * n1
                if money == Y:
                    return "{} {} {}".format(n10, n5, n1)
    return '-1 -1 -1'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
