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
    target = LI()

    target.sort()

    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if target[i] != target[j] != target[k]:
                    if target[k] < target[i] + target[j]:
                        ans += 1

    print(ans)


main()
