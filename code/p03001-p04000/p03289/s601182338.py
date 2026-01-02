import sys
from collections import deque
import copy

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    if S[0] != 'A':
        return 'WA'

    count = 0
    for i in range(1, len(S)):
        if i >= 2 and i <= len(S) - 2 and S[i] == 'C':
            count += 1
        else:
            if not (S[i] >= 'a' and S[i] <= 'z'):
                return 'WA'

    if count == 1:
        return "AC"

    return 'WA'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
