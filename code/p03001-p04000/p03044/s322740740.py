# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
	
def main():
	N = int(input())
	MP = Graph()
	
	for i in range(N-1):
		u, v, w = map(int, input().split(" "))
		u -= 1
		v -= 1
		if w % 2 == 0:
			MP.add_edge(u, v, 0)
			MP.add_edge(v, u, 0)
		else:
			MP.add_edge(u, v, 1)
			MP.add_edge(v, u, 1)
	
	tmp = Dijkstra(MP, 0)
	
	for i in range(N):
		if i == 0:
			print(0)
			continue
			
		tmptmp = tmp.shortest_distance(i)
		if tmptmp % 2 == 0:
			print(0)
		else:
			print(1)
			
	#print("---")
	#print(tmp.shortest_distance(1))
	
class Graph(object):
    # 隣接リストによる有向グラフ
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    # ダイクストラ法（二分ヒープ）による最短経路探索
    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
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
        # startノードからgoalノードまでの最短距離
        return self.dist[goal]

    def shortest_path(self, goal):
        # startノードからgoalノードまでの最短経路
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]
        
	
if __name__ == "__main__":
	main()
