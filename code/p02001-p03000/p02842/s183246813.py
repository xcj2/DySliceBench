#!/usr/bin/python3

import os
import sys


def main():
    N = read_int()
    ans = solve(N)
    if ans is None:
        print(':(')
    else:
        print(ans)


def solve(N):
    M = N * 100 // 108
    for d in range(20):
        if (M + d) * 108 // 100 == N:
            return M + d
        if (M - d) * 108 // 100 == N:
            return M - d
    return None


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
