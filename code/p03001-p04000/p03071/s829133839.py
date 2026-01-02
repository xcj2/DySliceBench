import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [a, b] = string_to_int(inputs[0])

    ret = 0
    if a > b:
        ret += a
        a -= 1
    else:
        ret += b
        b -= 1
    if a > b:
        ret += a
    else:
        ret += b

    return ret


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
