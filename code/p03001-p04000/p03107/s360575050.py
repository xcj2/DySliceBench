import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    count_0 = 0
    count_1 = 0

    for s in S:
        if s == "0":
            count_0 += 1
        else:
            count_1 += 1

    return len(S) - abs(count_0 - count_1)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
