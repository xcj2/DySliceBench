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
#input=sys.stdin.readline
show_flg=False
#=True

inf=float('inf')
n=I()
s=[[inf]*n for _ in range(n)]
g=[[] for i in range(n)]
for r in range(n):
    ri=list(input())
    for c in range(n):
        if ri[c]=='1':
            s[r][c]=1
            g[r].append(c)  

def wf(d):
    n=len(d)
    for k in range(n):#       // 経由する頂点
        for i in range(n):#    // 始点
            for j in range(n):#  // 終点
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

d=wf(s)
diam=-1
bg=0
ed=n-1
for r in range(n):
    for i,dist in enumerate(d[r]):
        if i==r:
            continue
        if diam<dist:
            diam=dist
            bg=r
            ed=i

v=[-1]*(n)

def bfs(x):
    p=deque()
    p.append(x)
    v[x]=0
    while p:
        c=p.popleft()
        for i in g[c]:
            if v[i]==-1:
                p.append(i)
                v[i]=v[c]+1
    return

bfs(bg)

for i in range(n):
    for nb in g[i]:
        if abs(v[nb]-v[i])!=1:
            print(-1)
            exit()
            #show(i,nb,v[i],v[nb])

print(diam+1)
exit()
'''
show(s)
show(wf(s))
show(diam,bg,ed)
show(v)
'''