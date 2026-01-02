#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,=pin()
    graph={i+1:dict() for i in range(N)}
    #print(graph)
    for i in range(N-1):
        u,v,w=pin()
        graph[u][v]=w%2
        graph[v][u]=w%2
    #print(graph)

    ans={i+1:0 for i in range(N)}
    seen={i+1:0 for i in range(N)}
    #ans[1]=0 (always)
    stack=[(1,0)]#pos,color
    while (stack!=[]):
        p,c=stack.pop()
        if seen[p]==1:continue

        seen[p]=1
        ans[p]=c
        for k,v in graph[p].items():
            stack.append((k,(c+v)%2))
    #print(ans)
    print(*ans.values(),sep="\n")
resolve()
