#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    A = LI()
    count = [0] * (N + 1)

    for a in A:
        count[a] += 1

    total = 0

    for idx in range(N+1):
        total += count[idx] * (count[idx] - 1) / 2
    for a in A:
        a_count = count[a]
        print(int(total - (a_count * (a_count - 1) /
                           2) + ((a_count - 1)*(a_count - 2)/2)))


main()
