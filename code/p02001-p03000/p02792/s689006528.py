#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    items = [[0 for i in range(9)]for j in range(9)]

    for i in range(N+1):
        start = int(str(i)[0])
        end = int(str(i)[-1])
        if end == 0:
            continue
        items[start - 1][end - 1] += 1

    ans = 0
    for i in range(9):
        for j in range(9):
            ans += items[i][j] * items[j][i]

    print(ans)


main()
