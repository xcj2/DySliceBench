from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
import random
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
def ItoS(nn):
    return chr(nn+97)
def GI(V,E,Directed=False,index=0):
    org_inp=[]
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        org_inp.append(inp)
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[0],inp[2])
            bb=(inp[1],inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return g,org_inp
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
show_flg=True

n,m=LI()
c=[]
x=[inf]*n
ans=True
g=[[] for _ in range(n)]
for i in range(m):
    l,r,d=LI_()
    d+=1
    g[l].append((r,d))
    g[r].append((l,-d))
    c.append((l,r,d))

v=[inf]*n
vs=[-1]*n

def bfs(st):
    if v[st]!=inf:
        return True
    q=[st]
    v[st]=0
    vs[st]=0
    while q:
        
        c=q.pop()
        for nb,d in g[c]:
            if vs[nb]==0:
                continue
            else:
                q.append(nb)
                vs[nb]=0
                if v[nb]==inf:
                    v[nb]=v[c]+d
                elif v[nb]!=v[c]+d:
                    show(c+1,nb+1,v)
                    return False
    return True

for i in range(n):
    if bfs(i):
        continue
    else:
        print('No')
        exit()

for i in range(m):
    l,r,d=c[i]
    if v[l]+d!=v[r]:
        print('No')
        exit()
        
print('Yes')


