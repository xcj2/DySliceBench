class Graph():  #directed
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.deg = [0 for _ in range(n)]
        for e in edge:
            self.graph[e[0] - indexed].append((e[1] - indexed, e[2]))
            self.deg[e[1] - indexed] += 1

    def dijkstra(self, s, INF=10**18, restore_to=None):
        dist = [INF for _ in range(self.n)]
        dist[s] = 0
        heap = [(0, s)]
        while heap:
            cost, node = heappop(heap)
            if dist[node] < cost:
                continue
            for adj, adjcost in self.graph[node]:
                if dist[node] + adjcost < dist[adj]:
                    dist[adj] = dist[node] + adjcost
                    heappush(heap, (dist[adj], adj))
        if restore_to is not None:
            g = restore_to
            if dist[g] == INF:
                return dist, False
            path = [g]
            node = g
            while node != s:
                node = prev[node]
                path.append(node)
            return dist, path[::-1]
        return dist

    def bellman_ford(self, s, t=None, INF=10**18):
        dist = [INF for _ in range(self.n)]
        dist[s] = 0
        update = True
        for i in range(self.n):
            update = False
            for node, g in enumerate(self.graph):
                for adj, adjcost in g:
                    if dist[node] != INF and dist[node] + adjcost < dist[adj]:
                        dist[adj] = dist[node] + adjcost
                        update = True
            if not update:
                return dist[t] if t is not None else dist
        if t is None:
            return
        negative_cycle = [0 for _ in range(self.n)]
        for i in range(self.n):
            for node, g in enumerate(self.graph):
                for adj, adjcost in g:
                    if dist[node] != INF and dist[node] + adjcost < dist[adj]:
                        dist[adj] = dist[node] + adjcost
                        negative_cycle[adj] = True
        if not negative_cycle[t]:
            return dist[t]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
E = []

for _ in range(M):
    a, b, c = map(int, input().split())
    E.append((a, b, -c))

g = Graph(N, E)
bf = g.bellman_ford(0, N - 1)

print(-bf if bf is not None else 'inf')