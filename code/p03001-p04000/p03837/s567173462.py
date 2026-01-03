#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D_fix_2
# CreatedDate:  2020-02-21 20:39:32 +0900
# LastModified: 2020-02-21 23:32:20 +0900
#


import heapq
def initial_signal(i,adj,N):
    d = [float("inf") for _ in range(N)]
    d[i] = 0
    Q = [(0,i)]
    return d,Q

def relax(n_cost, u, v, adj,d,Q):
    if d[v] > d[u]+n_cost:
        d[v]=d[u]+n_cost
        heapq.heappush(Q,(d[v],v))



def dijkstra(i,adj,N):
    d,Q = initial_signal(i,adj,N)
    while Q:
        cost, u = heapq.heappop(Q)
        for n_cost, v in adj[u]:
            relax(n_cost, u, v, adj, d, Q)
        
    return d



def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = map(int, input().split())
        adj[a-1].append((c,b-1))
        adj[b-1].append((c,a-1))
    shortest = []
    for i in range(N):
        shortest.append(dijkstra(i,adj,N))
    ans = 0
    for i in range(N):
        for cost, j in adj[i]:
            if cost>shortest[i][j]:
                ans+=1
    print(ans//2)


if __name__ == "__main__":
    main()
