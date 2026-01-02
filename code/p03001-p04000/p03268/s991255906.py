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

    counter = cl.Counter()

    for i in range(1, N + 1):
        amari = i % K
        counter.update({amari: 1})

    pairs = []

    for i in range(K):
        if (i * 2) % K == 0:
            pairs.append(i)

    ans = 0

    for pair in pairs:
        count = counter[pair]
        ans += count ** 3

    print(ans)


main()
