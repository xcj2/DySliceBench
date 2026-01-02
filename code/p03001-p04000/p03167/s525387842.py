#!/usr/bin/env python3
#dp7 #Grid 1

import sys
sys.setrecursionlimit(10000000)
def LI(): return list(map(int,sys.stdin.readline().split()))
def LIR(n): return [LI() for _ in range(n)]
mod = 10**9+7

def h():
    h,w = LI()
    grid = [list(input()) for _ in range(h)]

    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for j in range(w-1):
        if grid[0][j+1] == '.':
            dp[0][j+1] += dp[0][j]
            dp[0][j+1] %= mod
    for i in range(h-1):
        if grid[i+1][0] == '.':
            dp[i+1][0] += dp[i][0]
            dp[i+1][0] %= mod
    #(i,j)が空マスであるとき(i-1,j)および(i,j-1)からの移動が考えられる
    for i in range(1,h):
        for j in range(1,w):
            if grid[i][j] == '.':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[i][j] %= mod
    print(dp[-1][-1])
if __name__ == '__main__':
    h()
