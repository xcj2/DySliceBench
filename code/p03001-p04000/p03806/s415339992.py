#!/usr/bin/env python3

from copy import deepcopy

ABMAX = 400
HUGE = 10 ** 12

def main():
    n, ma, mb = map(int, input().split())
    sold = []
    for i in range(n):
        a, b, c = map(int, input().split())
        sold.append((a, b, c))
    mincost = dp(sold, n)
    print(find_mincost(mincost, ma, mb))

def find_mincost(mincost, ma, mb):
    res = HUGE
    for mult in range(1, ABMAX):
        if ma * mult > ABMAX:
            break
        if mb * mult > ABMAX:
            break
        res = min(res, mincost[ma * mult][mb * mult])
    return -1 if res == HUGE else res

def dp(sold, n):
    # mincost[a][b]: Minimum cost of achieving a, b
    mincost = [[HUGE for b in range(ABMAX + 1)] for a in range(ABMAX + 1)]
    mincost[0][0] = 0
    for a, b, c in sold:
        update(mincost, a, b, c)
    return mincost

def update(mincost, a, b, c):
    for ia in reversed(range(ABMAX + 1)):  # 配る
        for ib in reversed(range(ABMAX + 1)):
            na = ia + a
            nb = ib + b
            if na <= ABMAX and nb <= ABMAX:
                mincost[na][nb] = min(mincost[na][nb], mincost[ia][ib] + c)

main()
