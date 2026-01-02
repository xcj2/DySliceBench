import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    transpotation = [
        int(inputs[1]),
        int(inputs[2]),
        int(inputs[3]),
        int(inputs[4]),
        int(inputs[5])
    ]

    bottleneck = 0

    for t in transpotation:
        if bottleneck == 0 or t < bottleneck:
            bottleneck = t
    power_bottleneck = math.ceil(N / bottleneck)
    return power_bottleneck + 4


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(6))
    print(ret)
