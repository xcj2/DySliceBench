# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial,sqrt
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n=I() #n:頂点数　w:辺の数

d = [[float("inf")]*n for i in range(n)]
lis=[LI() for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(n):
    for j in range(i+1,n):
        d[i][j]=lis[i][j]
        d[j][i]=lis[i][j]
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
warshall_floyd(d)
sm=0
for i in range(n):
    sm+=sum(lis[i])
#インデックスで与えられていることに注意
#ソース　https://juppy.hatenablog.com/entry/2018/11/01/蟻本_python_全点対最短経路法（ワーシャルフロイド法
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if d[i][j]!=lis[i][j]:
            print(-1)
            sys.exit()
        if d[i][j]==lis[i][j]:
            for k in range(n):
                if i!=k!=j and d[i][k]+d[k][j]==d[i][j]:
                    count+=lis[i][j]
                    #print(i,j,k)
                    break
print(sm//2-count)


                

        

    
            
        
        
    

    
        
    
    
    