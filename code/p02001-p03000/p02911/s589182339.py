#!/usr/bin/python3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, K, Q, A):
    solved = [0] * N
    for a in A:
        solved[a] += 1

    def qualified(n):
        return Q - n < K

    return [qualified(n) for n in solved]


def main():
    N, K, Q = [int(e) for e in inp().split()]
    A = [int(input()) - 1 for _ in  range(Q)]

    ans = solve(N, K, Q, A)
    for a in ans:
        print('Yes' if a else 'No')


if __name__ == '__main__':
    main()
