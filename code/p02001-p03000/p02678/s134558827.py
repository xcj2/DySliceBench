#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
from collections import deque
def resolve():
    N,M=pin()
    edge=dict()
    for i in range(M):
        a,b=pin()
        #non-directed
        edge.setdefault(a,[])
        edge.setdefault(b,[])
        edge[a].append(b)
        edge[b].append(a)
    #print(edge)
    milestones=[0]*(N+1)#1-index
    milestones[1]=1
    c=deque([1])
    #print(c)
    while(1):
        if len(c)==0:
            break
        t=c.popleft()
        #print(t)
        for to in edge[t]:
            #print(f"to={to}")
            if milestones[to]==0:
                milestones[to]=t
                c.append(to)
        #print(c)
        ##print(f"milestones={milestones}")
        ##print(f"endt={t}")
    print("Yes")
    print(*milestones[2:],sep="\n")
        
#%%submit!
resolve()