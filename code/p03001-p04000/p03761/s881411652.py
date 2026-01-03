import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs
    counters = []

    for s in S:
        c = collections.Counter(list(s))
        counters.append(c)

    n_counter = {}
    last = counters.pop()
    for k in last.keys():
        min_c = last[k]
        exist = True
        for c in counters:
            if k not in c:
                exist = False
                break
            else:
                if min_c > c[k]:
                    min_c = c[k]
        if exist:
            n_counter[k] = min_c
    ret = []
    for a in sorted(n_counter.keys()):
        ret += [a for _ in range(n_counter[a])]
    return ''.join(ret)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
