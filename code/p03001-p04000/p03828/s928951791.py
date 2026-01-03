import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    SSSS = 1000000007
    count = collections.Counter()

    for i in range(1, N+1):
        target = i
        is_end = False
        while not is_end:
            is_end = True
            for j in range(2, int(math.sqrt(target)+1)):
                if target % j == 0:
                    count[j] += 1
                    target = target // j
                    is_end = False
                    break
            if is_end and target != 1:
                count[target] += 1
    c = 1
    for k, v in count.items():
        c *= (v + 1)
        c = c % SSSS
    return c


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
