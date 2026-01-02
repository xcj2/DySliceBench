import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = list(inputs[0])
    ACGT = {"A", "C", "G", "T"}

    max_length = 0
    for i in range(0, len(S)):
        length = 0
        j = i
        while j < len(S) and S[j] in ACGT:
            length += 1
            j += 1
        max_length = length if length > max_length else max_length
    return max_length


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
