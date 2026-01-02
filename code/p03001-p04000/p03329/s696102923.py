import sys
from collections import deque
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    n = int(inputs[0])
    LIMIT = 100000
    sixs = [6]
    nines = [9]
    while sixs[-1] <= LIMIT:
        sixs.append(6 * sixs[-1])
    sixs.pop()
    while nines[-1] <= LIMIT:
        nines.append(9 * nines[-1])
    nines.pop()

    choises = [1]
    choises.extend(sixs)
    choises.extend(nines)

    # [count]
    dp = [0]

    for i in range(1, n+1):
        candidates = []
        for c in choises:
            if i - c >= 0:
                candidates.append(dp[i-c] + 1)
        dp.append(min(candidates))

    return dp[-1]


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
