#!/usr/bin/python3

import os
import sys


def main():
    L, K = read_ints()
    print(solve(L, K))


def solve(L, K):
    D = [[0, 0] for _ in range(L + 1)]
    D[1][0] = 1
    if K <= L:
        D[K][0] = 1

    for i in range(1, L):
        D[i + 1][1] += D[i][0]
        D[i + 1][0] += D[i][1]
        if i + K <= L:
            D[i + K][0] += D[i][1]

    return sum([D[i][0] for i in range(1, L + 1)])


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

