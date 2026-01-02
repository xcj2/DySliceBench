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
    A = [0] + string_to_int(inputs[0]) + [0]
    all_cost = 0
    position = 0
    for a in A:
        all_cost += abs(position - a)
        position = a
    all_cost += abs(position)

    costs = []
    # 0 3 5 -1 0
    for i, a in enumerate(A):
        if i == 0 or i == len(A) - 1:
            continue
        cost = all_cost \
            - abs(A[i] - A[i-1]) \
            - abs(A[i+1] - A[i]) \
            + abs(A[i+1] - A[i-1])
        costs.append(cost)
    return costs


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    for r in ret:
        print(r)
