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
def graph():
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=inpm()
        a-=1
        b-=1
        g[a].append(b)
        g[b].append(a)
    return n,m,g
 
def main():
    n,q=inpm()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=inpm()
        a-=1
        b-=1
        g[a].append(b)
        g[b].append(a)
    tuple(g)
    px=[]
    for _ in range(q):
        px.append(tuple(inpl()))
    ans=[0 for _ in range(n)]
    went=[False for _ in range(n)]
    went[0]=True
    for i in range(q):
        ans[px[i][0]-1]+=px[i][1]
    que=deque()
    que.append(0)
    while que:
        par = que.pop()
        for chi in g[par]:
            if went[chi]:
                continue
            else:
                went[chi]=True
                ans[chi]+=ans[par]
                que.append(chi)
    
    print(*ans)

if __name__ == "__main__":
    main()