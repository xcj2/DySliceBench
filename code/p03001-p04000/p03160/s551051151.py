#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	A
# CreatedDate:  2020-02-22 17:51:25 +0900
# LastModified: 2020-02-22 20:24:45 +0900
#


import os
import sys
import heapq
def initial_signal(i,N):
    d = [float("inf") for _ in range(N)]
    d[i] = 0
    Q = []
    heapq.heappush(Q,(0,i))
    return d, Q

def dijkstra(i,adj,N):
    d,Q = initial_signal(i,N)
    while Q:
        u_value,u = heapq.heappop(Q)
        for v_value,v in adj[u]:
            if d[v]>d[u]+v_value:
                d[v]=d[u]+v_value
                heapq.heappush(Q,(d[v],v))
    print(d[-1])



def main():
    N = int(input())
    h = list(map(int,input().split()))
    adj = [[] for _ in range(N)]
    for i in range(N-2):
        adj[i].append((abs(h[i+1]-h[i]),i+1))
        adj[i].append((abs(h[i+2]-h[i]),i+2))
    adj[N-2].append((abs(h[N-1]-h[N-2]),N-1))
    dijkstra(0,adj,N)


if __name__ == "__main__":
    main()
