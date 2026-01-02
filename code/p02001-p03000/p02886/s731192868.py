#!/usr/bin/python3

import array
import math
import os
import sys


def main():
    N = read_int()
    D = read_ints()
    s = 0
    for i in range(N):
        for j in range(i + 1, N):
            s += D[i] * D[j]
    print(s)


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
