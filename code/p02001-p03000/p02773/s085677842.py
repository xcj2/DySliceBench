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

    counter = cl.Counter()
    for i in range(N):
        s = input()
        counter.update({s: 1})
    item, value = zip(*counter.most_common())
    ans = []
    max_num = value[0]
    for i in range(len(value)):
        if value[i] == max_num:
            ans.append(item[i])

    ans.sort()
    print(*ans, sep="\n")


main()
