#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()

    pairs = []

    for i in range(N):
        x, y = MI()
        pairs.append((x, y))

    modified = []

    max_a = -1 * 10 ** 9
    min_a = 10 ** 9
    max_b = -1 * 10 ** 9
    min_b = 10 ** 9

    for i in range(len(pairs)):
        x, y = pairs[i]
        modified.append([x - y, x + y])

        max_a = max(max_a, x-y)
        min_a = min(min_a, x-y)
        max_b = max(max_b, x+y)
        min_b = min(min_b, x+y)

    ans = max(max_a - min_a, max_b - min_b)
    print(ans)


main()
