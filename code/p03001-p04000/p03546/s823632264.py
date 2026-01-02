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
    H, W = MI()
    costs = []

    for i in range(10):
        cost_row = LI()
        costs.append(cost_row)

    for k in range(10):
        for i in range(10):
            for j in range(10):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    ans = 0
    for _ in range(H):
        row = LI()
        for item in row:
            if item == -1:
                continue
            ans += costs[item][1]

    print(ans)


main()
