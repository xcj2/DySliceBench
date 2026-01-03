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

def prim(n,g):
    edgelist = []
    used = [False for _ in range(n)]
    for edge in g[0]:
        heappush( edgelist, edge)
    used[0] = True
    res = 0 

    while len(edgelist)>0:
        minedge = heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = True
        for edge in g[v]:
            if not used[edge[1]]:
                heappush( edgelist, edge)
        res += minedge[0]
    return res

def main():
    n=inp()
    xy=[]
    for index in range(n):
        x,y = inpm()
        xy.append((x,y,index))
        
    g=[[] for _ in range(n)]
    xy.sort()
    for i in range(n-1):
        j = i+1
        w = min(abs(xy[i][0]-xy[j][0]),abs(xy[i][1]-xy[j][1]))
        a = xy[i][2]
        b = xy[j][2]
        g[a].append((w,b))
        g[b].append((w,a))
    xy.sort(key=lambda y:y[1])
    for i in range(n-1):
        j = i+1
        w = min(abs(xy[i][0]-xy[j][0]),abs(xy[i][1]-xy[j][1]))
        a = xy[i][2]
        b = xy[j][2]
        g[a].append((w,b))
        g[b].append((w,a))
    print( prim(n,g) )

if __name__ == "__main__":
    main()