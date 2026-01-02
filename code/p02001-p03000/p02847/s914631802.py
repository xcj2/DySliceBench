#!/usr/bin/python3

import os
import sys


def main():
    S = inp()

    D = ['SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
    i = D.index(S)
    print(i + 1)


###############################################################################

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
