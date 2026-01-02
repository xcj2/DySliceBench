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
    a = LI()

    half = N // 2
    ans = []
    ans.extend(a)
    for i in range(half - 1, -1, -1):
        sum_later = 0
        for j in range(2 * i + 1, N, i + 1):
            sum_later += ans[j]

        amari = sum_later % 2
        if amari == a[i]:
            ans[i] = 0
        else:
            ans[i] = 1
    print(sum(ans))
    for i in range(len(ans)):
        if ans[i] == 1:
            print(i + 1)


main()
