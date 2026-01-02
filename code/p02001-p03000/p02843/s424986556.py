#!/usr/bin/python3

import os
import sys


def main():
    X = read_int()
    print('1' if solve(X) else '0')


def solve(X):
    c = X // 100
    for d in range(6):
        n = c - d
        if n < 0:
            break
        r = X - 100 * n
        if 0 <= r <= n * 5:
            return True
    return False


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
