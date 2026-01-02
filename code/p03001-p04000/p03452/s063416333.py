import sys
input = sys.stdin.readline
from collections import deque
import marshal


class Graph:
    class Edge:
        def __init__(self, to, cost):
            """
            :param to:  終点ノード
            :param cost: 辺の重み
            """
            self.to, self.cost = to, cost

    def __init__(self, n, directed=False, decrement=True, destroy=False, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.destroy = destroy
        self.edges = [[] for _ in range(self.n)]
        self.dist = [None] * self.n
        self.info = [-1]*self.n
        for x, y, cost in edges:
            self.add_edge(x, y, cost)

    def add_edge(self, x, y, cost):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].append(self.Edge(y, cost))
        if self.directed == False:
            self.edges[y].append(self.Edge(x, cost))

    def bfs(self, start, goal=-1, time=0, save=False):
        """
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: （ループがあっても）最短距離。存在しなければ -1
        """
        if self.decrement:
            start -= 1
            goal -= 1
        if not save:
            self.dist = [None] * self.n
        p, t, dist = start, time, 0
        self.dist[p] = 0
        next_set = deque([(p, t, dist)])

        while next_set:
            p, t, dist = next_set.popleft()
            for edge in self.edges[p]:
                q, cost = edge.to, edge.cost
                if self.dist[q] is not None:
                    if self.dist[q] != dist + cost:
                        print("No")
                        exit()
                    continue
                self.dist[q] = dist + cost
                next_set.append((q, t + 1, dist + cost))
        return True

##################################################################################################

N, M = map(int, input().split())
graph = Graph(N, directed=True, decrement=True, destroy=False)
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph.add_edge(x, y, cost)
    graph.add_edge(y, x, -cost)
for i in range(1,N+1):
    if graph.dist[i-1] is None:
        graph.bfs(i, goal=-1, time=0, save=True)
print("Yes")