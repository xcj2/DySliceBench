import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    questions = []
    for i in range(1, len(inputs)):
        questions.append(string_to_int(inputs[i]))

    cumulative_sum = [0]
    for i in range(0, len(S)-1):
        if S[i] == "A" and S[i+1] == "C":
            cumulative_sum.append(cumulative_sum[-1] + 1)
        else:
            cumulative_sum.append(cumulative_sum[-1])

    results = []
    for [start, end] in questions:
        results.append(cumulative_sum[end-1] - cumulative_sum[start-1])

    return results


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [_, N] = string_to_int(input())
    ret = solve(inputs(N+1))
    for r in ret:
        print(r)
    # print(ret)
