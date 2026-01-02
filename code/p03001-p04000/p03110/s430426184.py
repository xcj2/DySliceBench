import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    BTC_TO_YEN = 380000.0
    result = 0.0
    otoshidama = [i.split() for i in inputs]
    for o in otoshidama:
        if o[1] == "BTC":
            result += float(o[0]) * BTC_TO_YEN
        else:
            result += float(o[0])
    return result


def string_to_float(string):
    return list(map(lambda x: float(x), string.split()))


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
