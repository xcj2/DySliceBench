# -*- coding: utf-8 -*-
"""
D - Practical Skill Test
https://beta.atcoder.jp/contests/abc089/tasks/abc089_d

"""
import sys
from sys import stdin
input = stdin.readline


def sub_solve(l, r):
    sx, sy = numbers[l]
    gx, gy = numbers[r]
    return abs(sx - gx) + abs(sy - gy)


def solve(queries, H, W, D):
    dp = [0] * (H*W+1)
    for i in range(D+1, H*W+1):
        dp[i] = dp[i-D] + sub_solve(i-D, i)

    for l, r in queries:
        ans = dp[r] - dp[l]
        print(ans)


numbers = dict()
def main(args):
    global numbers
    H, W, D = map(int, input().split())

    for y in range(1, H+1):
        tmp = [int(x) for x in input().split()]
        for x, i in enumerate(tmp, start=1):
            numbers[i] = (x, y)

    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append([int(x) for x in input().split()])

    solve(queries, H, W, D)


if __name__ == '__main__':
    main(sys.argv[1:])
    
