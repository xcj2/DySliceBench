from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=sys.stdin.readline
show_flg=False
#show_flg=True

n,m,R=MI()
r=LI_()
g=[[] for _ in range(n)]
for i in range(m):
    a,b,c=LI_()
    g[a].append((b,c+1))
    g[b].append((a,c+1))

show(g)
inf=float('inf')
def wf(e):
    n=len(e)
    d=[[inf]*n for _ in range(n)]
    for a in range(n):
        for b,c in g[a]:
            d[a][b]=c
            d[b][a]=c
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j]>d[i][k]+d[j][k]:
                    d[i][j]=d[i][k]+d[j][k]
    
    return d

ans=inf
md=wf(g)
dists=[]
def search(st,d,ls):
    if len(ls)==1:
        dists.append(d+md[st][ls[0]])
        return
    for gl in ls:
        search(gl,d+md[st][gl],[i for i in ls if i!=gl])
    return

for i in r:search(i,0,[j for j in r if i!=j])
print(min(dists))
