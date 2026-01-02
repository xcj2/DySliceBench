# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, M = map(int, input().split())


class Dijkstra(object):
    """ ある特定の点からそのほかの頂点への最小距離を求める
    最短区間を実現するルートについては、prevに格納していく
    """
    def __init__(self, n:int):
        self.adjacency_dict = {}
        self.n = n
        for i in range(n):
            self.add_vertex(i)

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = {}

    def add_edge(self, v1: int, v2: int, w: float, undirected=False):
        self.adjacency_dict[v1][v2] = w
        if undirected:
            self.adjacency_dict[v2][v1] = w

    def run(self, start: int) -> (list, list):
        """ startから初めてそれ以外のノードへの最短距離をダイクストラ法で求める """
        # sからの距離とその前のノードを管理する
        dist = [float('inf')] * self.n
        prev = [None] * self.n
        heap_q = []

        dist[start] = 0

        # プライオリティキューでstartから各ノードの(最短距離, ノードindex)を管理する
        heappush(heap_q, (0, start))

        while len(heap_q) > 0:
            # 未確定な中から最小のノードを取得し、確定する
            d, l = heappop(heap_q)

            # 最小のノードから直接リンクしているノードについて、距離が縮まるようであれば更新する
            for node in self.adjacency_dict[l].keys():
                new_dist = dist[l] + self.adjacency_dict[l][node]
                if dist[node] > new_dist:
                    dist[node] = new_dist
                    heappush(heap_q, (new_dist, node))
                    prev[node] = l

        return dist, prev


g = Dijkstra(N)
for _ in range(M):
    v1, v2 = map(int, input().split())
    g.add_edge(v1 - 1, v2 - 1, 1, undirected=True)

# print(g.adjacency_dict)

dist, prev = g.run(start=0)
# print(dist)

print('Yes')
for p in prev[1:]:
    print(p+1)
