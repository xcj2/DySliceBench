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
    stations = list(map(string_to_int, inputs))
    N = len(stations)
    ret = []
    for i, s in enumerate(stations):
        [C, S, F] = s
        t = S + C
        for j in range(i+1, N):
            if t < stations[j][1]:
                t = stations[j][0] + stations[j][1]
            else:
                w = (t - stations[j][1]) % stations[j][2]
                waiting = 0 if w == 0 else stations[j][2] - w
                t += waiting + stations[j][0]
        ret.append(t)
    ret.append(0)
    return ret


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N-1))
    for r in ret:
        print(r)
