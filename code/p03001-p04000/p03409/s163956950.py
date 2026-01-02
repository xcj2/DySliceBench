# https://atcoder.jp/contests/abc091/tasks/arc092_a

import sys
input = sys.stdin.readline
from collections import deque


class MaxFlow:
    class Edge:
        def __init__(self, to, cap, rev):
            """
            :param to:  終点ノード
            :param cap: 残された容量
            :param rev: 遂になる逆向きのエッジ（ノード to の rev 番目のエッジ）
            """
            self.to, self.cap, self.rev = to, cap, rev

    def __init__(self, node_size, inf):
        self._node = node_size
        self._inf = inf
        self._level = [-1] * self._node
        self._iter = [0] * self._node
        self._graph = [[] for _ in range(self._node)]

    def add_edge(self, from_, to, cap):
        self._graph[from_].append(self.Edge(to, cap, len(self._graph[to])))
        self._graph[to].append(self.Edge(from_, 0, len(self._graph[from_]) - 1))

    def bfs(self, start):
        """
        _level: 未訪問の場合は -1, 訪問済みの場合は start からの最短距離（正容量のエッジのみを使った経路の中での）
        """
        self._level = [-1] * self._node
        next_set = deque()
        self._level[start] = 0
        next_set.append(start)
        while next_set:
            cur_vertex = next_set.popleft()
            for edge in self._graph[cur_vertex]:
                if self._level[edge.to] < 0 < edge.cap:
                    self._level[edge.to] = self._level[cur_vertex] + 1
                    next_set.append(edge.to)

    def dfs(self, cur_vertex, end_vertex, flow):
        if cur_vertex == end_vertex:
            return flow
        while self._iter[cur_vertex] < len(self._graph[cur_vertex]):
            edge = self._graph[cur_vertex][self._iter[cur_vertex]]
            if edge.cap > 0 and self._level[cur_vertex] < self._level[edge.to]:
                flowed = self.dfs(edge.to, end_vertex, min(flow, edge.cap))
                if flowed > 0:
                    edge.cap -= flowed
                    self._graph[edge.to][edge.rev].cap += flowed
                    return flowed
            self._iter[cur_vertex] += 1
        return 0

    def solve(self, source, sink):
        flow = 0
        while True:
            self.bfs(source)
            if self._level[sink] < 0:
                """ sinkへの最短距離が -1 ⇒ sink にたどり着けない ⇒ 増加路が存在しないため探索終了"""
                return flow
            self._iter = [0] * self._node
            while True:
                f = self.dfs(source, sink, self._inf)
                if f == 0:
                    break
                flow += f


class Dinic:
    def __init__(self, len_X, len_Y):
        """
        soursの位置 = 0
        sinkの位置  = len_X + len_Y + 1
        capacity   = 1
        の最大フロー問題
        """
        self.len_X, self.len_Y = len_X, len_Y
        self.mf = MaxFlow(self.len_X + self.len_Y + 2, min(self.len_X, self.len_Y))
        for i in range(self.len_X):
            """ sours から部分集合Xへの各点に capacity=1 の流れを作る """
            self.mf.add_edge(0, i + 1, 1)
        for i in range(self.len_Y):
            """ 部分集合Yへの各点からsinkへの capacity=1 の流れを作る """
            self.mf.add_edge(self.len_X + i + 1, self.len_X + self.len_Y + 1, 1)

    def add_edge(self, from_, to):
        """
        :param from_: 部分集合Xの頂点　（1,...,len_X）
        :param to:    部分集合Yの頂点　（len_X + 1,...,len_X + 1 + len_Y）
        """
        self.mf.add_edge(from_ + 1, to + self.len_X + 1, 1)

    def solve(self):
        return self.mf.solve(0, self.len_X + self.len_Y + 1)

#####################################################################################

N = int(input())

X = []
Y = []
for i in range(N):
    X.append([int(i) for i in input().split()])

for i in range(N):
    Y.append([int(i) for i in input().split()])

dinic = Dinic(len(X), len(Y))

for i in range(len(X)):
    for j in range(N):
        if X[i][0] < Y[j][0] and X[i][1] < Y[j][1]:
            dinic.add_edge(i,j)


print(dinic.solve())