# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=jp

4.73[s]??§????????????AC
"""
from enum import Enum
from heapq import heappush, heappop


class Sssp(object):
    """ single source shortest path """
    class Status(Enum):
        """ ?????????????¨??????¶??? """
        white = 1  # ????¨????
        gray = 2  # ?¨???????
        black = 3  #?¨???????

    def __init__(self, V, data):
        num_of_nodes = V
        self.color = [Sssp.Status.white] * num_of_nodes  # ????????????????¨??????¶???
        self.d = [float('inf')] * num_of_nodes  # ?§???????????????????
        self.p = [-1] * num_of_nodes  # ????????????????????????????¨?????????????????????????
        self.adj = [[] for _ in range(num_of_nodes)]
        self.make_adj(data)


    def make_adj(self, data):
        # ??£??\??????????????????
        for f, t, c in data:
            self.adj[f].insert(0, (t, c))
            # self.adj[t].insert(0, (f, c))

    def dijkstra(self, start):
        self.d[start] = 0
        pq = []
        heappush(pq, (0, start))

        while pq:
            cost, u = heappop(pq)
            self.color[u] = Sssp.Status.black
            if self.d[u] < cost:
                continue

            for v, cost in self.adj[u]:
                if self.color[v] == Sssp.Status.black:
                    continue
                if self.d[v] > self.d[u] + cost:
                    self.d[v] = self.d[u] + cost
                    heappush(pq, (self.d[v], v))
                    self.color[v] = Sssp.Status.gray


def solve(V, r, data):
    WHITE = 0
    GRAY = 1
    BLACK = 2
    num_of_nodes = V
    color = [WHITE] * num_of_nodes  # ????????????????¨??????¶???
    d = [float('inf')] * num_of_nodes  # ?§???????????????????
    adj = [[] for _ in range(num_of_nodes)]

    for f, t, c in data:
        adj[f].insert(0, (t, c))

    # dijkstra
    d[r] = 0
    pq = []
    heappush(pq, (0, r))

    while pq:
        cost, u = heappop(pq)
        color[u] = BLACK
        if d[u] < cost:
            continue

        for v, cost in adj[u]:
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                heappush(pq, (d[v], v))
                color[v] = GRAY

    # ???????????¨???
    for i in range(V):
        if d[i] == float('inf'):
            print('INF')
        else:
            print('{}'.format(d[i]))


if __name__ == '__main__':
    # ??????????????\???
    V, E, r = [int(x) for x in input().split(' ')]
    data = []
    for i in range(E):
        data.append(list(map(int, input().split(' '))))

    # ???????????¢?´¢
    solve(V, r, data)