#!/usr/bin/env python3
#dp5 #Knapsack 2
#個数制限ありナップサック
#1≤W≤10**9
import sys
def LI(): return list(map(int, sys.stdin.readline().split()))
def LIR(n): return [LI() for _ in range(n)]
def e():
    n,W = LI()
    wv = LIR(n)

    #横:価値　縦:品物
    dp = [[float("inf") for _ in range(10**5+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1,n+1):
        for j in range(10**5+1):
            #i番目の品物の価値より価値の制限が小さいとき(i番目の品物が使えないとき)
            if j < wv[i-1][1]:
                #i-1番目の品物の重さと同じ
                dp[i][j] = dp[i-1][j]
            else:
                #i番目の品物を使い、重さを追加する場合と使わない場合の重さを比較
                dp[i][j] = min(dp[i-1][j],dp[i-1][j - wv[i-1][1]] + wv[i-1][0])
    ans = 0
    #重さWまでの価値最大値
    for i in range(10**5+1):
        if dp[n][i] <= W:
            ans = i
    print(ans)
if __name__ == '__main__':
    e()
