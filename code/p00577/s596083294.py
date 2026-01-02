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
    S = inp()
    print(solve(N, S))


def solve(N, S):
    i = 0
    count = 0
    while i < N - 1:
        if S[i] != S[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    return count


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

