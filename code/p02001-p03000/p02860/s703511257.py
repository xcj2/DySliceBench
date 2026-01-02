#!/usr/bin/python3

import os
import sys


def main():
    N = read_int()
    S = inp()
    print('Yes' if N % 2 == 0 and S[N // 2:] == S[:N // 2] else 'No')


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
