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
    A = read_ints()
    print(solve(N, A))


def solve(N, A):
    height_map = {}
    for i, a in enumerate(A):
        if a not in height_map:
            height_map[a] = []
        height_map[a].append(i + 1)

    heights = list(height_map)
    heights.sort(reverse=True)

    landscape = [0] * (N + 2)
    count = 0
    best = 0
    for h in heights:
        if h == 0:
            break
        for i in height_map[h]:
            l, r = landscape[i - 1], landscape[i + 1]
            if l == 0 and r == 0:
                count += 1
            elif l == 1 and r == 1:
                count -= 1
            landscape[i] = 1

        best = max(best, count)

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

