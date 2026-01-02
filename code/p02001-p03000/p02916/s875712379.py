#!/usr/bin/python3

import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, A, B, C):
    sat = B[A[0]]
    for i in range(1, N):
        sat += B[A[i]]
        if A[i - 1] + 1 == A[i]:
            sat += C[A[i - 1]]
    return sat


def main():
    N = int(inp())
    A = [int(e) - 1 for e in inp().split()]
    B = [int(e) for e in inp().split()]
    C = [int(e) for e in inp().split()]
    print(solve(N, A, B, C))


if __name__ == '__main__':
    main()
