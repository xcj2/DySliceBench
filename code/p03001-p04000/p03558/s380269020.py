# -*- coding: utf-8 -*-
import sys
from heapq import heappush,heappop
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
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
    
    K=int(input())
    edges=[[] for _ in range(K)]
    for i in range(K):
        edges[i].append((1,(i+1)%K))
        edges[i].append((0,i*10%K))
    d=dijkstra(1,K,edges)
    print(d[0]+1)

if __name__ == '__main__':
    main()
