import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m,r=map(int,input().split())
rlst=list(map(int,input().split()))
abc=[list(map(int,input().split())) for i in range(m)]

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
    x-=1
    y-=1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
lst=warshall_floyd(d)
# print(lst)
pro=list(permutations(range(r)))
# print(pro)
ans=float('inf')
for i in pro:
    tmp=0
    for j in range(r-1):
        now=i[j]
        nxt=i[j+1]
        tmp+=lst[rlst[now]-1][rlst[nxt]-1]
    ans=min(ans,tmp)
print(ans)