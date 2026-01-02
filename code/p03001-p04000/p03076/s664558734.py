#!/usr/bin/env python3
import sys
import itertools
import collections
import functools
import math
from queue import Queue
# import numpy as np
INF = float("inf")


def solve(A: int, B: int, C: int, D: int, E: int):
    ryouri = [A, B, C, D, E]
    a = [x % 10 for x in ryouri if x % 10 != 0]
    if len(a) == 0:
        print(sum([10*(math.ceil(x/10.0)) for x in ryouri]))
    else:
        print(sum([10*(math.ceil(x/10.0)) for x in ryouri]) - (10-min(a)))

    # print(A, B, C, D, E)
    # print(A+B+C+D+E)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(A, B, C, D, E)


if __name__ == '__main__':
    main()
