import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [A, B, K] = string_to_int(inputs[0])
    results = []
    small = A if A > B else B
    for i in reversed(range(1, small+1)):
        if A % i == 0 and B % i == 0:
            results.append(i)
    return results[K-1]


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
