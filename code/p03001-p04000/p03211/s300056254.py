import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = list(inputs[0])
    min_diff = -1
    for i in range(0, len(S)-2):
        value = int(S[i] + S[i+1] + S[i+2])
        diff = abs(753 - value)
        if min_diff == -1 or diff < min_diff:
            min_diff = diff
    return min_diff


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
