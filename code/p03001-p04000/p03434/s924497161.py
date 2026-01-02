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
    cards = string_to_int(inputs[0])
    cards.sort(reverse=True)
    count_a = 0
    count_b = 0
    turn_a = True
    for card in cards:
        if turn_a:
            count_a += card
        else:
            count_b += card
        turn_a = not turn_a
    return count_a - count_b


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
