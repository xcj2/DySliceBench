import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
def input():
    return sys.stdin.readline()[:-1]

def dfs(v,prev = -1):
    for u in graph[v]:
        if u == prev:
            continue
        sign[u] = v
        dfs(u,v)

def bfs(v):
    que = deque([])
    que.append(v)
    while que:
        p = que.popleft()
        if visited[p] == 0:
            visited[p] = 1
            for u in graph[v]:
                que.append(u)

import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * (N+1) # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for u in graph[v]:
            tmp = 1 + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                path[u] = v
                heapq.heappush(hq, (tmp, u))
    return path

N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
path = [0]*(N+1)
c = dijkstra(1)
print("Yes")
for i in range(2,N+1):
    print(c[i])
