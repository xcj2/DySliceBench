#!/usr/bin/python3

import array
import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


INF = 2 ** 31 - 1


def solve(N, M, A, B, C):
    D = []
    for c in C:
        b = 0
        for v in c:
            b |= 1 << (v - 1)
        D.append(b)

    bits = 1 << N
    dp = array.array('i', [INF] * bits)

    dp[0] = 0
    for a, d in zip(A, D):
        for b in range(bits):
            if dp[b] == INF:
                continue
            nb = b | d
            dp[nb] = min(dp[nb], dp[b] + a)

    if dp[bits - 1] == INF:
        return -1
    return dp[bits - 1]


def main():
    N, M = [int(e) for e in inp().split()]
    A = []
    B = []
    C = []
    for _ in range(M):
        a, b = [int(e) for e in inp().split()]
        c = [int(e) for e in inp().split()]
        A.append(a)
        B.append(b)
        C.append(c)
    print(solve(N, M, A, B, C))


if __name__ == '__main__':
    main()
