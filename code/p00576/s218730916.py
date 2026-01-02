#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    N = read_int()
    X = read_ints()
    M = read_int()
    A = read_ints()
    print(*solve(N, X, M, A), sep='\n')


def solve(N, X, M, A):
    ar = [0] * 2020
    pos = [0] * (N + 1)
    for i, x in enumerate(X):
        ar[x] = i + 1
        pos[i + 1] = x

    for a in A:
        x = pos[a]
        if x != 2019 and ar[x + 1] == 0:
            ar[x] = 0
            ar[x + 1] = a
            pos[a] = x + 1

    return pos[1:]


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

