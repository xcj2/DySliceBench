#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


MOD = 10 ** 9 + 7


def main():
    N = II()
    targets = LI()

    colors = [0] * 3
    ans = 1

    for i in range(N):
        count = 0
        for k in range(3):
            if colors[k] == targets[i]:
                if count == 0:
                    colors[k] += 1
                count += 1
        ans *= count
        ans %= MOD

    print(ans)


main()
