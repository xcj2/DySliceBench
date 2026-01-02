import sys
from collections import deque
import copy

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    if _solve(N):
        return 'Yes'
    return 'No'


def _solve(n):
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        ret = []
        ret.append(_solve(n - 7))
        ret.append(_solve(n - 4))
        return any(ret)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
