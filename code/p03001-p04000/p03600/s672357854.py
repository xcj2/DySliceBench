from collections import defaultdict
from heapq import heappop, heappush
from itertools import combinations

class Graph:
    def __init__(self, n, edges, weight=False):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.degree = [0] * n
        self.weight = defaultdict(lambda: 10**18)
        if weight:
            for u, v, weight in edges:
                self.adj[u].append(v)
                self.adj[v].append(u)
                self.degree[v] += 1
                self.weight[(u, v)] = weight
                self.weight[(v, u)] = weight
        else:
            for u, v in edges:
                self.adj[u].append(v)
                self.adj[v].append(u)
                self.degree[v] += 1
                self.weight[(u, v)] = 1
                self.weight[(v, u)] = 1

    def dijkstra(self, start, goal=None):  # O((n+m)log(n))
        INF = 10**18
        dist = [INF] * self.n
        dist[start] = 0
        heap = [(0, start)]  # (dist, v)
        sp_prev = [None] * self.n  # previous node in shortest path (sp)
        while heap:
            dist_v, v = heappop(heap)
            if dist[v] < dist_v:
                continue
            for adj in self.adj[v]:
                edge_weight = self.weight[(v, adj)]
                if dist[v] + edge_weight < dist[adj]:
                    dist[adj] = dist[v] + edge_weight
                    sp_prev[adj] = v
                    heappush(heap, (dist[adj], adj))

        if goal is not None:
            if dist[goal] == INF:
                return dist, []
            else:
                path = [goal]
                v = goal
                while v != start:
                    v = sp_prev[v]
                    path.append(v)
                path.reverse()
                return dist, path
        else:
            return dist, sp_prev

    def warshall_floyd(self):  # O(n^3)
        # dist[u][v]: uからvへの最短距離
        INF = 10**18
        dist = [[INF] * self.n for _ in range(self.n)]
        for u in range(self.n):
            dist[u][u] = 0
            for v in self.adj[u]:
                dist[u][v] = self.weight[(u, v)]
        for k in range(self.n):
            for u in range(self.n):
                for v in range(self.n):
                    dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
        return dist

# ---------------------- #

n = int(input())
A = [tuple(int(x) for x in input().split()) for _ in range(n)]
dist = []
for i in range(n):
    for j in range(n):
        if i < j:
            dist.append((i, j, A[i][j]))

G = Graph(n, dist, weight=True)
wf = G.warshall_floyd()

for i in range(n):
    for j in range(n):
        if A[i][j] != wf[i][j]:
            print(-1)
            exit()

ans = 0
for i, j in combinations(range(n), 2):
    for k in range(n):
        if i == k or j == k:
            continue
        if A[i][j] == A[i][k] + A[k][j]:
            break
    else:
        ans += A[i][j]

print(ans)
