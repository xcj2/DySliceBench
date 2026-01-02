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
    [A] = string_to_int(inputs[0])
    [B] = string_to_int(inputs[1])
    [C] = string_to_int(inputs[2])
    [D] = string_to_int(inputs[3])
    [E] = string_to_int(inputs[4])
    foods = [A, B, C, D, E]
    time = 0

    while len(foods) > 0:
        optimal_f = -1
        optimal_i = -1
        for i, f in enumerate(foods):
            futility = (time + f) % 10
            if futility == 0:
                optimal_i = i
                break
            if futility > optimal_f or optimal_f == -1:
                optimal_f = futility
                optimal_i = i
        time += foods[optimal_i]
        foods.pop(optimal_i)
        if len(foods) != 0 and time % 10 != 0:
            time += 10 - (time % 10)
    return time


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(5))
    print(ret)
