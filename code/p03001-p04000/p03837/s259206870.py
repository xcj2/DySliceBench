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

def dijkstra(edge,st):
    # edge=[[(v_to,dist_to_v),...],[],...]
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else inf,i) for i in range(n)]
    prev=[0]*n
    q=[i for i in d]
    heapify(q)
    
    # calc
    while q:
        dist,cur=heappop(q)
        for dst,dist in edge[cur]:
            alt=d[cur][0]+dist
            if alt<d[dst][0]:
                d[dst]=(alt,dst)
                prev[dst]=cur
                heappush(q,(alt,dst))
    return d,prev
    
show_flg=False
show_flg=True

ans=0
n,m=LI()
g,ip=GI(n,m)
mins=[]
for i in range(n):
    d,p=dijkstra(g,i)
    mins.append([i for i,j in d])

for a,b,c in ip:
    k=1
    for y in range(n):
        if y==b:
            continue
        if mins[y][a]+c==mins[y][b]:
            k=0
    ans+=k

print(ans)
