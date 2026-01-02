import heapq
import sys
input = sys.stdin.readline

N, M, S, T = map(int, input().split())

import heapq


class Edge():
    """ 重み付き有向辺 """

    def __init__(self, _to, _cost):
        self.to = _to
        self.cost = _cost


class Dijkstra():
    def __init__(self, V):

        self.G = [[] for i in range(V+1)]
        self._E = 0
        self._V = V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加"""
        self.G[_from].append(Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路リスト 
        """
        que = []
        heapq.heapify(que)
        d = [float("inf")] * (self._V+1)
        d[s] = 0
        heapq.heappush(que, (0, s))  

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost:
                continue

            for i in range(len(self.G[v])):
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost
                    heapq.heappush(que, (d[e.to], e.to))
        return d
graph_snuke = Dijkstra(N)
graph_yen = Dijkstra(N)
for _ in range(M):
    u, v, a, b = map(int, input().split())
    graph_yen.add(u, v, a)
    graph_yen.add(v, u, a)
    graph_snuke.add(u, v, b)
    graph_snuke.add(v, u, b)

yen = graph_yen.shortest_path(S)
snuke = graph_snuke.shortest_path(T)
minimum_case = [10**15 for i in range(N+1)]
for i in range(N):
    minimum_case[1+i] -= (yen[i+1]+snuke[i+1])
for i in range(N-1, -1, -1):
    minimum_case[i] = max(minimum_case[i], minimum_case[i+1])
for i in range(1, N+1):
    print(minimum_case[i])