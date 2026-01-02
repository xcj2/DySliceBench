#!/usr/bin/python3

import os
import sys


def main():
    V, E, R = read_ints()
    D = [tuple(read_ints()) for _ in range(E)]
    print(*solve(V, E, R, D), sep='\n')


def solve(V, E, R, D):
    INF = 10001 * 1000
    dists = [INF] * V
    dists[R] = 0
    for _ in range(V - 1):
        for s, t, d in D:
            if dists[s] != INF and dists[t] > dists[s] + d:
                dists[t] = dists[s] + d

    for s, t, d in D:
        if dists[s] != INF and dists[s] + d < dists[t]:
            return ['NEGATIVE CYCLE']

    return ['INF' if d == INF else d for d in dists]


###############################################################################
# AUXILIARY FUNCTIONS

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

