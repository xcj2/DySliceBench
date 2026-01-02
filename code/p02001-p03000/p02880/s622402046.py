#!/usr/bin/python3

import array
import math
import os
import sys


def main():
    N = read_int()
    for x in range(1, 10):
        for y in range(x, 10):
            if x * y == N:
                print('Yes')
                return
    print('No')


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
