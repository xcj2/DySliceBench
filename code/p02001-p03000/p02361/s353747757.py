from heapq import heappush, heappop

class Dijkstra:
    def __init__(self, N):
        self.N = N # #vertices
        self.E = [[] for _ in range(N)]

    def add_edge(self, init, end, weight, undirected=False):
        self.E[init].append((end, weight))
        if undirected: self.E[end].append((init, weight))
    
    def distance(self, s):
        INF = float('inf')
        E, N = self.E, self.N
        self.dist = dist = [INF] * N # the distance of each vertex from s
        self.prev = prev = [-1] * N # the previous vertex of each vertex on a shortest path from s
        dist[s] = 0
        n_visited = 0 # #(visited vertices)
        heap = []
        heappush(heap, (0, s))
        while heap:
            d, v = heappop(heap)
            if dist[v] < d: continue # (s,v)-shortest path is already calculated
            for u, c in E[v]:
                temp = d + c
                if dist[u] > temp:
                    dist[u] = temp; prev[u] = v
                    heappush(heap, (temp, u))
            n_visited += 1
            if n_visited == N: break
        return dist
    
    def shortest_path(self, t):
        P = []
        prev = self.prev
        while True:
            P.append(t)
            t = prev[t]
            if t == -1: break
        return P[::-1]
    
N, M, r = map(int, input().split())
dk = Dijkstra(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    dk.add_edge(a, b, c)
dist = dk.distance(r)
for d in dist:
    if d == float('inf'): print('INF')
    else: print(d)
