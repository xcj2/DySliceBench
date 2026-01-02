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
    A = LI()

    counter_add = cl.Counter()
    counter_sub = cl.Counter()
    for i in range(N):
        add = i + 1 + A[i]
        sub = i + 1 - A[i]
        counter_add.update({str(add): 1})
        counter_sub.update({str(sub): 1})

    ans = 0
    for key, val in counter_add.items():
        ans += val * counter_sub[key]

    print(ans)


main()
