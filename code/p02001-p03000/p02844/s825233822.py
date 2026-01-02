#!/usr/bin/python3

import os
import sys


def main():
    N = read_int()
    S = inp()
    print(solve(N, S))


def solve(N, S):
    D = set()
    D.add('')
    R = set()

    for ch in S:
        for d in list(D):
            if len(d) == 2:
                R.add(d + ch)
            else:
                D.add(d + ch)
    return len(R)


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
