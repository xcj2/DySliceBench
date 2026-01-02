#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    while True:
        N, M = read_ints()
        if (N, M) == (0, 0):
            break
        P = [read_ints() for _ in range(M)]
        print(solve(N, M, P))


def solve(N, M, P):
    T = [[P[j][i] for j in range(M)] for i in range(N)]
    return max([sum(t) for t in T])


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

