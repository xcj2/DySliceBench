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


def solve(N, K, S):
    A = []
    i = 0
    while i < N:
        j = i
        while j < N and S[j] == S[i]:
            j += 1
        A.append(j - i)
        i = j

    assert sum(A) == N
    cur = N - len(A)
    return min(cur + 2 * K, N - 1)


def main():
    N, K = [int(e) for e in inp().split()]
    S = inp()
    print(solve(N, K, S))


if __name__ == '__main__':
    main()
