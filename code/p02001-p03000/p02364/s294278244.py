class Graph:
    class Edge:
        def __init__(self, to, cost):
            """
            :param to:  終点ノード
            :param cost: 辺の重み
            """
            self.to, self.cost = to, cost

    def __init__(self, n, directed=False, decrement=True, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.edges = [[] for _ in range(self.n)]
        self.edges2 = []                            # ワーシャルフロイド用
        self.parent = [-1]*self.n
        self.info = [-1]*self.n
        for x, y, cost in edges:
            self.add_edge(x, y, cost)

    def add_edge(self, x, y, cost):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].append(self.Edge(y, cost))
        self.edges2.append((x, y, cost))
        if self.directed == False:
            self.edges[y].append(self.Edge(x, cost))
            self.edges2.append((y, x, cost))

    def prim(self):
        """
        :return: 最小全域木を選んだ時の重さの総和
        """
        start = 0  # 解析のスタート地点を決める。どこでもいい
        visit = [False] * self.n  # 各頂点までの最短距離
        next_set = [(0, start)]
        res = 0
        while next_set:
            dist, p = heappop(next_set)  # 近いところから順に確定させていく必要があるため、heappop を用いる
            if visit[p]:
                continue
            visit[p] = True
            res += dist  # クラスカル法と違って隣接点を調べていくので、足される数の大きさはバラバラ
            for edge in self.edges[p]:
                q, cost = edge.to, edge.cost
                if visit[q]:
                    continue
                heappush(next_set, (cost, q))  # q を介して他の頂点に行く可能性を考える。q に行くまでの最短距離が明らかになっている点が重要
        return res

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        if self.directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        for x in range(self.n):
            for edge in self.edges[x]:
                G.add_edge(x + self.decrement, edge.to + self.decrement, weight=edge.cost)


        edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.axis("off")
        plt.show()

##############################################################################################################
import sys
input = sys.stdin.readline
from heapq import *


N, M = map(int, input().split())
graph = Graph(N, directed=False, decrement=True)
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph.add_edge(x, y, cost)

print(graph.prim())
