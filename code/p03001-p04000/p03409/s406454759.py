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
    int_inputs = list(map(string_to_int, inputs))
    N = len(inputs) // 2
    reds = int_inputs[:N]
    blues = int_inputs[N:]

    reds.sort(key=lambda x: x[0])
    blues.sort(key=lambda x: x[0])

    count = 0
    for bi in range(N):
        candidates = []
        for ri in range(len(reds)):
            if blues[bi][0] > reds[ri][0] and blues[bi][1] > reds[ri][1]:
                candidates.append([ri, reds[ri][0], reds[ri][1]])
        if len(candidates) > 0:
            candidates.sort(key=lambda x: x[2])

            reds.pop(candidates[-1][0])
            count += 1

    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N*2))
    print(ret)
