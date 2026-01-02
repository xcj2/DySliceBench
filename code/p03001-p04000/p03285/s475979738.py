#!/usr/bin/env python3
import sys
import itertools
import collections
import functools
import math
from queue import Queue
# import numpy as np
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int):
    for i in range(26):
        for j in range(15):
            if i*4+j*7 == N:
                yes()
                return
    no()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
