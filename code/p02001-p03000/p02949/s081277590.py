import math
from collections import deque

def BellmanFord(edges, N, M, start):
    dist = [math.inf]*N
    dist[start] = 0

    for i in range(N):
        for j in range(M):
            if is_valid(edges[j][0], edges[j][1]):
                if dist[edges[j][1]] > dist[edges[j][0]] + edges[j][2]:
                    dist[edges[j][1]] = dist[edges[j][0]] + edges[j][2]
                    if i == N - 1:
                        return False

    return dist

def dfs(graph, N, start):
    visited = [False]*N
    visited[start] = True
    q = deque([start])

    while q:
        v = q.pop()
        for n_v in graph[v]:
            if not visited[n_v]:
                visited[n_v] = True
                q.append(n_v)
    
    return visited

def is_valid(f, t):
    return can_from_start[f] and can_from_start[t] and can_to_goal[f] and can_to_goal[t]


N, M, P = map(int, input().split())
graph = [[] for _ in range(N)]
graph_inv = [[] for _ in range(N)]
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A - 1].append(B - 1)
    graph_inv[B - 1].append(A - 1)
    edges.append((A - 1, B - 1, - (C - P)))

can_from_start = dfs(graph, N, 0)
can_to_goal = dfs(graph_inv, N, N - 1)

dist = BellmanFord(edges, N, M, 0)

if dist:
    print(max(0, -dist[N - 1]))
else:
    print(-1)