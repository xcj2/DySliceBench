from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
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
    return [ord(i)-97 +10 for i in input()]
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

#sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

def BellmanFord(graph,num_v,source=0):
    # graph = 隣接リスト g[source]=[(destination, dist),...]
    # edgeの初期化 edge = [(source,destination,dist),...]
    edges=[]
    for u in range(num_v):
        for v,d in graph[u]:
            edges.append((u,v,d))
    inf=float("inf")
    dist=[inf for i in range(num_v)]
    dist[source]=0
    neg=[False for i in range(num_v)]
    neg_flg=False
    
    #辺の緩和
    for i in range(num_v):
        if i==num_v-1:
            check=dist[n-1]
        for u,v,d in edges:
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                if i==num_v-1:# and neg[v]==True:
                    # N回目で更新があったという事は負閉路が存在する
                    neg_flg=True
                neg[v] = True
    if neg_flg:
        for i in range(num_v):
            for u,v,d in edges:
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
    if dist[n-1]==check:
        neg_flg=False
    return neg_flg,dist
 

show_flg=False
show_flg=True

n,m=LI()
g=[[] for i in range(n)]

for i in range(m):
    a,b,c=LI_()
    c=-c-1
    g[a].append((b,c))
    #g[b].append((a,c))
    #show((a,b,-c))

fl,d=BellmanFord(g,n,0)
if fl:
    ans='inf'
else:
    ans=-d[n-1]
print(ans)