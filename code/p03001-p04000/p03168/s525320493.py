#!/usr/bin/env python3
#dp8 #Coin

import sys
sys.setrecursionlimit(10000000)
def LI(): return list(map(float,sys.stdin.readline().split()))
def LIR(n): return [LI() for _ in range(n)]
mod = 10**9+7

def I():
    n = int(input())
    p = LI()
    #縦:コインの枚数,横:表が出た回数
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(n+1):
            dp[i][j] = p[i-1]*dp[i-1][j-1]+(1-p[i-1])*dp[i-1][j]
    print(sum(dp[n][n//2+1:n+1]))





if __name__ == '__main__':
    I()
