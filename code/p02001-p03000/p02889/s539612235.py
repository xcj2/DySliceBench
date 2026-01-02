import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product

def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m,l=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]
q=int(input())
st=[list(map(int,input().split())) for i in range(q)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n,w = n,m #n:頂点数　w:辺の数

d = [[float("inf") for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = abc[i]
    x,y=x-1,y-1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
tmp=warshall_floyd(d)

newd = [[float("inf") for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if d[i][j]<=l:
            newd[i][j]=1
            newd[j][i]=1
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０

tmp=warshall_floyd(newd)

for i in range(q):
    s,t=st[i]
    s,t=s-1,t-1

    print(newd[s][t]-1 if newd[s][t]!=float('inf') else -1)