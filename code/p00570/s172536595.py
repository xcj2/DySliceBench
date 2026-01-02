#!/usr/bin/python3

import os
import sys


def main():
    N, K = read_ints()
    T = [read_int() for _ in range(N)]
    print(solve(N, K, T))


def solve(N, K, T):
    diffs = [T[i + 1] - T[i] for i in range(N - 1)]
    diffs.sort()
    t = N
    for i in range(N - K):
        t += diffs[i] - 1
    return t


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

