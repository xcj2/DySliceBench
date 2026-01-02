import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    [T, A] = string_to_int(inputs[1])
    H = string_to_int(inputs[2])

    min_diff = -1
    min_diff_i = -1
    for i, h in enumerate(H):
        t = T - h * 0.006
        diff = abs(A-t)
        if min_diff == -1 or diff < min_diff:
            min_diff = diff
            min_diff_i = i
    return min_diff_i + 1


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(3))
    print(ret)
