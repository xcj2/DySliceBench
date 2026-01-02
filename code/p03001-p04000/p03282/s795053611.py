import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = list(inputs[0])
    K = int(inputs[1])

    if len(S) == 1:
        return int(S[0])

    for i, c in enumerate(S):
        if c == '1' and K == i + 1:
            return 1
        elif c != '1':
            return int(c)

    # count = 0
    # for i, c in enumerate(S):
    #     print(int(c) ** (49 * (10**14))
    #     # count += int(c) ** (49 * (10**14))
    #     # if count > K:
    #     #     return S[i-1]
    # return c


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
