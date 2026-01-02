import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, M, X, Y] = string_to_int(inputs[0])
    x = string_to_int(inputs[1])
    y = string_to_int(inputs[2])
    max_x = max(x)
    min_y = min(y)

    candidates = [x for x in range(max_x+1, min_y+1)]
    for c in candidates:
        if c > X and c <= Y:
            return "No War"
    return "War"


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(3))
    print(ret)
