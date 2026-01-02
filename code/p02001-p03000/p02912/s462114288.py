#!/usr/bin/python3

from fractions import Fraction
import heapq
import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, A):
    hq = [-a for a in A]
    heapq.heapify(hq)
    for _ in range(M):
        v = -hq[0]
        if v < 1:
            break
        v = Fraction(v, 2)
        heapq.heapreplace(hq, -v)

    return sum([math.floor(-v) for v in hq])


def main():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    print(solve(N, M, A))


if __name__ == '__main__':
    main()
