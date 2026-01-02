#!/usr/bin/env python3
import collections as cl
import sys

MOD = 10 ** 9 + 7


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N, M = MI()
    isbroken = [False] * (N + 1)
    for i in range(M):
        a = II()
        isbroken[a] = True

    steps = [0] * (N + 1)

    steps[0] = 1
    if not isbroken[1]:
        steps[1] = 1
    for i in range(2, N + 1):
        if isbroken[i]:
            continue
        steps[i] = steps[i - 1] + steps[i - 2]
        steps[i] %= MOD
    print(steps[-1])


main()
