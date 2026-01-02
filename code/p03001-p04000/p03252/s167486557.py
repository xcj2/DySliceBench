import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    T = inputs[1]

    appeared = {}
    appeared_count = {}
    for i, _ in enumerate(S):
        if T[i] in appeared:
            if not appeared[T[i]] == S[i]:
                return "No"
        else:
            appeared[T[i]] = S[i]
            if S[i] in appeared_count:
                appeared_count[S[i]] += 1
            else:
                appeared_count[S[i]] = 1
    for k, v in appeared_count.items():
        if v > 1:
            return "No"
    return "Yes"


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
