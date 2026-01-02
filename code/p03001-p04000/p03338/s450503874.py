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
    s = inputs[0]
    max_count = 0
    for i in range(1, len(s)):
        front = s[0:i]
        tail = s[i:]
        front_kind = set()
        tail_kind = set()

        for f in front:
            front_kind.add(f)

        for t in tail:
            tail_kind.add(t)

        count = len(front_kind & tail_kind)
        max_count = max([count, max_count])
    return max_count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
