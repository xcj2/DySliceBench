import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, C, inputs1, inputs2):
    B = string_to_int(inputs1)
    A = list(map(lambda i: string_to_int(i), inputs2))

    num = 0
    for a in A:
        score = 0
        for i in range(0, M):
            score += a[i] * B[i]
        score += C

        if score > 0:
            num += 1

    return num


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M, C] = string_to_int(input())
    ret = solve(N, M, C, input(), inputs(N))
    print(ret)
