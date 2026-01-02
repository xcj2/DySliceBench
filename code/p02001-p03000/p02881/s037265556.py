#!/usr/bin/python3

import array
import math
import os
import sys


def main():
    N = read_int()
    print(solve(N))


def solve(N):
    best = N - 1
    x = 2
    while x * x <= N:
        if N % x == 0:
            y = N // x
            best = min(best, x + y - 2)
        x += 1
    return best


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
