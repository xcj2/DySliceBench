from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random  # randome is not available at Codeforces
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
inf=float('inf')
#eps=10**(-10)
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
show_flg=True

def wf(d):
    n=len(d)
    for k in range(n):#       // 経由する頂点
        for i in range(n):#    // 始点
            for j in range(n):#  // 終点
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


n,m,l=MI()
d=[[inf]*n for _ in range(n)]
for i in range(m):
    a,b,c=LI_()
    d[a][b]=c+1
    d[b][a]=c+1

d=wf(d)
g=[[inf]*n for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if d[i][j]<=l:
            g[i][j]=1
            g[j][i]=1
g=wf(g)

q=I()
for _ in range(q):
    s,t=LI_()
    if g[s][t]==inf:
        ans=-1
    else:
        ans=g[s][t]-1
    print(ans)
    
