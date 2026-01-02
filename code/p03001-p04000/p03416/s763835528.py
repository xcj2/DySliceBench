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
    [A, B] = string_to_int(inputs[0])
    count = 0
    for n in range(A, B+1):
        s = str(n)
        front = []
        back = []
        if len(s) % 2 == 0:
            half = len(s) // 2
            front = list(s[:half])
            back = list(s[half:])
        else:
            half = len(s) // 2
            front = list(s[:half])
            back = list(s[half+1:])
        if front == list(reversed(back)):
            count += 1
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
