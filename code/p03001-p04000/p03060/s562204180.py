import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N] = string_to_int(inputs[0])
    V = string_to_int(inputs[1])
    C = string_to_int(inputs[2])

    ret = 0
    for i, _ in enumerate(V):
        if V[i] - C[i] > 0:
            ret += V[i] - C[i]
    return ret


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(3))
    print(ret)
