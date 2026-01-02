#!/usr/bin/python3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(S):
    N = len(S)
    a = 0
    ans = 0
    i = 0
    while i < N:
        if S[i] == 'A':
            a += 1
            i += 1
            continue
        if S[i:i + 2] == 'BC':
            ans += a
            i += 2
            continue
        a = 0
        i += 1
    return ans


def main():
    print(solve(inp()))


if __name__ == '__main__':
    main()
