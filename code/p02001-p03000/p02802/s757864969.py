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
    n, m = MI()

    isACed = [0] * n
    submmited = [0] * n

    for i in range(m):
        p, res = input().split()
        p = int(p)
        if isACed[p - 1] == 0 and res == "WA":
            submmited[p - 1] += 1

        if res == "AC":
            isACed[p - 1] = 1
    acs = 0
    was = 0
    for i in range(n):
        if isACed[i] == 1:
            acs += 1
            was += submmited[i]

    print(acs, was, sep=" ")


main()
