import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    persons = list(inputs[0])

    count = [persons[1:].count("E")]

    for i in range(1, len(persons)):
        if i == 0:
            continue

        tmp = count[-1]
        if persons[i - 1] == 'W':
            tmp += 1
        if persons[i] == 'E':
            tmp -= 1
        count.append(tmp)

    return min(count)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
