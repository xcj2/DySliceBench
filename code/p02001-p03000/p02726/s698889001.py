# -*- coding: utf-8 -*-
import sys
from heapq import heappush,heappop
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,X,Y=map(int,input().split())
    X-=1
    Y-=1
    
    def dijkstra(start,n,edges):
        d=[INF]*n
        used=[False]*n
        d[start]=0
        used[start]=True
        edgelist=[]
        for edge in edges[start]:
            heappush(edgelist,edge)
        while edgelist:
            minedge=heappop(edgelist)
            if used[minedge[1]]:
                continue
            v=minedge[1]
            d[v]=minedge[0]
            used[v]=True
            for edge in edges[v]:
                if not used[edge[1]]:
                    heappush(edgelist,(edge[0]+d[v],edge[1]))
        return d
    
    edges=[[] for _ in range(N)]
    for i in range(N-1):
        edges[i].append((1,i+1))
        edges[i+1].append((1,i))
    edges[X].append((1,Y))
    edges[Y].append((1,X))

    ans=[0]*N
    for i in range(N):
        d=dijkstra(i,N,edges)
        for x in d:
            ans[x]+=1
    for row in ans[1:]:
        print(row//2)

if __name__ == '__main__':
    main()
