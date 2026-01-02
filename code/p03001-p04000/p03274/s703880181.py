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
    N, K = MI()
    targets = LI()
    if N == 1:
        print(abs(targets[0]))
        return
    length = targets[K - 1] - targets[0]
    ans = length + min(abs(targets[K-1]), abs(targets[0]))
    for i in range(N-K + 1):
        length = targets[i + K - 1] - targets[i]
        cost = length + min(abs(targets[i+K-1]), abs(targets[i]))
        ans = min(ans, cost)

    print(ans)


main()
