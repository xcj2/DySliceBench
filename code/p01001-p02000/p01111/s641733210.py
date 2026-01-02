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
        B = read_int()
        if B == 0:
            break
        print(*solve(B))


def solve(B):
    bb = 2 * B

    lb = 1
    ub = B + 1
    while ub - lb > 1:
        m = (lb + ub) // 2
        if m * m <= bb:
            lb = m
        else:
            ub = m

    n = lb
    while True:
        if bb % n == 0:
            k = bb // n
            if (k - n) % 2 == 1:
                return (k - n + 1) // 2, n
        n -= 1


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

