#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    A, B, C = read_ints()
    print(solve(A, B, C))


def solve(A, B, C):
    weekly = A * 7 + B
    weeks = C // weekly
    rest = C - weekly * weeks
    days = (rest + A - 1) // A
    if days > 7:
        days = 7
    return weeks * 7 + days


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

