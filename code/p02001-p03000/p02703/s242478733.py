class Graph:
    class Edge:
        def __init__(self, to, cost, fare):
            """
            :param to:  終点ノード
            :param cost: 辺の重み
            """
            self.to, self.cost, self.fare = to, cost, fare

    def __init__(self, n, directed=False, decrement=True, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.edges = [[] for _ in range(self.n)]
        self.parent = [-1]*self.n
        self.info = [-1]*self.n
        self.fare_max = 0
        for x, y, cost, fare in edges:
            self.add_edge(x, y, cost, fare)
            if fare > self.fare_max:
                self.fare_max = fare

    def add_edge(self, x, y, cost, fare):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].append(self.Edge(y, cost, fare))
        if self.directed == False:
            self.edges[y].append(self.Edge(x, cost, fare))
        if fare > self.fare_max:
            self.fare_max = fare

    def cut(self, x):
        return min2(x, self.fare_max * (self.n - 1))

    def dijkstra(self, start, S, INF=10**18):
        """
        :param start: スタート地点
        :return: スタート地点から各点への距離のリスト
        備考: heqpq の比較のための key は第一引数である点に注意（ =　heappush(heapq, (key,value))　）
        """
        res = [[INF] * (self.fare_max*self.n+1) for _ in  range(self.n)]
        if self.decrement:
            start -= 1
        money = self.cut(S)
        res[start][money] = 0
        next_set = [(0, start, money)]
        while next_set:
            dist, p, money = heappop(next_set)
            if res[p][money] < dist:
                continue
            for edge in self.edges[p]:
                q, cost, fare = edge.to, edge.cost, edge.fare
                temp_d = dist + cost
                if temp_d < res[q][self.cut(money-fare)] and money >= fare:
                    res[q][self.cut(money-fare)] = temp_d
                    heappush(next_set, (temp_d, q, self.cut(money - fare)))
        if self.decrement:
            return [[0]] + res
        else:
            return res

def max2(x,y):
    return x if x > y else y

def min2(x,y):
    return x if x < y else y



##############################################################################################################

import sys
input = sys.stdin.readline
from heapq import *
INF = 10**18  # 大きい数字

C, D = [], []
N, M, S = map(int, input().split())

graph = Graph(N, directed=False, decrement=True)
for _ in range(M):
    x, y, fare, cost = map(int, input().split())
    graph.add_edge(x, y, cost, fare)
for i in range(1,N+1):
    fare, cost = map(int, input().split())
    graph.add_edge(i,i, cost, -fare)
d = graph.dijkstra(1,S,INF=INF)
for i in range(2,N+1):
    print(min(d[i]))