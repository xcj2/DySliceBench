#!/usr/bin/env python3
import sys
from collections import defaultdict
from heapq import heappop, heappush


class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):

    def __init__(self, graph, start):
        self.g = graph.graph

        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]

def solve(N: int, M: int, L: "List[int]", R: "List[int]", C: "List[int]"):
    graph= Graph()
    for i in range(M):
        graph.add_edge(L[i]-1,R[i]-1,C[i])
    for i in range(N-1):
        graph.add_edge(i+1,i,0)
    d = Dijkstra(graph,0)
    shortest = d.shortest_distance(N-1)
    
    if shortest == float('inf'):
        print(-1)
    else:
        print(shortest)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, L, R, C)

if __name__ == '__main__':
    main()
