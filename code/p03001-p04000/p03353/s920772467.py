import sys
from functools import reduce
import copy
import math


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    K = int(inputs[1])

    sets = set()
    for i in range(len(S)):
        j = i
        while j < len(S) and j - i <= K:
            j += 1
        sets.add(S[i:j])
    new_sets = set()

    for k in sets:
        for i in range(len(k)):
            j = i
            while j < len(k) and j - i <= K:
                j += 1
                new_sets.add(k[i:j])
    l = list(new_sets)
    l.sort()
    return l[K-1]


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
