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
    h,w = map(int,input().split()) #n:頂点数　w:辺の数
    d = []
    for _ in range(10):
        d.append(inpl())
    n=10
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    a=[]
    for _ in range(h):
        a.append(inpl())
    pre = []
    for i in range(10):
        pre.append(d[i][1])
    check = defaultdict(int)
    for i in range(h):
        for j in range(w):
            if a[i][j]==-1:
                continue
            check[a[i][j]]+=1
    ans=0
    for i in range(10):
        ans += pre[i]*check[i]
    print(ans)

def main(): 
    warshall_floyd()

if __name__ == "__main__":
    main()