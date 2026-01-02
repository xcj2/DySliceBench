#!/usr/bin/python3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, V):
    M = N // 2

    def build(off):
        d = dict()
        for i in range(off, N, 2):
            if V[i] not in d:
                d[V[i]] = 0
            d[V[i]] += 1

        arr = []
        for k, v in d.items():
            arr.append((M - v, k))

        arr.append((M, -1))

        arr.sort()
        return arr

    A = build(0)
    B = build(1)

    best = N
    for c1, v1 in A:
        for c2, v2 in B:
            if v1 != v2:
                best = min(best, c1 + c2)
                break
    return best


def main():
    N = int(inp())
    V = [int(e) for e in inp().split()]
    assert len(V) == N
    print(solve(N, V))


if __name__ == '__main__':
    main()
