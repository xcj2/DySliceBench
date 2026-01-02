#!/usr/bin/env python3
import sys
import itertools
import collections
import functools
import math
from queue import Queue
# import numpy as np
INF = float("inf")


def solve(a: int, b: int, c: int, d: int, e: int, k: int):
    if e-a > k:
        print(":(")
    else:
        print("Yay!")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    e = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(a, b, c, d, e, k)


if __name__ == '__main__':
    main()
