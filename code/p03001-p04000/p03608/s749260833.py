from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
# import numpy as np
# import scipy
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7

def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])

def graphm():
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(m):
        a,b,w=inpm()
        a-=1
        b-=1
        g[a].append((w,b))
        g[b].append((w,a))
    return n,m,g

def warshall_floyd(): # d[i][j]: iからjへの最短距離
    n,m,r = map(int,input().split()) #n:頂点数　w:辺の数
    R=inpl()
    d=[[10**10 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        x,y,z = inpm()
        x -= 1
        y -= 1
        d[x][y] = z
        d[y][x] = z
    for i in range(n):
        d[i][i] = 0 #自身のところに行くコストは0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    ans = float('inf')
    for com in permutations(R,r):
        ans_pre = 0
        for i in range(r-1):
            ans_pre += d[com[i]-1][com[i+1]-1]
        ans = min(ans,ans_pre)
    print(ans)

def main(): 
    warshall_floyd()

if __name__ == "__main__":
    main()