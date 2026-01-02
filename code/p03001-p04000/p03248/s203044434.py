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

    if S[0] == '0' or S[-1] == '1':
        return None

    for i in range((N - 1) // 2):
        if S[i] != S[-2 - i]:
            return None

    mxsz = 1
    for i in range((N - 2) // 2):
        if S[i + 1] == '1':
            mxsz = i + 2

    G = []
    # print(mxsz)
    root = mxsz + 1
    croot = root

    for i in range(root - 1, 0, -1):
        G.append((croot, i))
        if S[i - 1] == '1':
            croot = i

    for i in range(mxsz + 2, N + 1):
        G.append((root, i))

    return G


def main():
    ans = solve(inp())
    if ans is None:
        print('-1')
        return
    for (p, q) in ans:
        print(p, q)


if __name__ == '__main__':
    main()
