import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def change_color(t):
    if t == '0':
        return '1'
    return '0'


def solve(inputs):
    tiles = list(inputs[0])
    tiles = [x == "1" for x in tiles]

    diff_num_1 = 0
    diff_num_2 = 0
    state_1 = True
    state_2 = False

    for t in tiles:
        if t != state_1:
            diff_num_1 += 1
        if t != state_2:
            diff_num_2 += 1

        state_1 = not state_1
        state_2 = not state_2
    return min(diff_num_1, diff_num_2)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
