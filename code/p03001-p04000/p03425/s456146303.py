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
    persons = inputs
    N = 5
    kinds = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0, }
    for n in persons:
        if n[0] in kinds:
            kinds[n[0]] += 1
    kinds_list = list(kinds.keys())

    if len(persons) < 3:
        return 0

    pattern = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                p1 = kinds_list[i]
                p2 = kinds_list[j]
                p3 = kinds_list[k]
                pattern += kinds[p1] * kinds[p2] * kinds[p3]
    return pattern


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
