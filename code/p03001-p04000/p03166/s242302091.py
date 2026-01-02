#!/usr/bin/env python3
#dp6 #Longest-Path

import sys
sys.setrecursionlimit(10000000)
def LI(): return list(map(int,sys.stdin.readline().split()))
def LIR(n): return [LI() for _ in range(n)]
def g():
    def dfs(x):
        #既に最長パスがわかっている頂点はそれを返す
        if dp[x] != None:
            return dp[x]
        #移動できる頂点がないとき0
        if len(Graph[x]) == 0:
            dp[x] = 0
            return 0
        else:
            res = 0
            #移動できる頂点の中で最大パスをもつものを探す
            for y in Graph[x]:
                res = max(res,dfs(y)+1)
            dp[x] = res
            return dp[x]

    n,m = LI()
    #dpで各頂点を始点とした最大パスを管理
    dp = [None for _ in range(n)]
    Graph = [[] for _ in range(n)]
    for _ in range(m):
        x,y = LI()
        Graph[x-1].append(y-1)
    #各頂点を始点として最大パスを探す
    for i in range(n):
        dfs(i)
    print(max(dp))
if __name__ == '__main__':
    g()
