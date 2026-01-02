import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines


# rstrip().decode('utf-8')
# INF=float("inf")
#MOD=10**9+7
sys.setrecursionlimit(2147483647)
# import math
#import numpy as np
# import operator
#import bisect
from heapq import heapify,heappop,heappush
#from math import gcd
# from fractions import gcd
#from collections import deque
from collections import defaultdict
# from collections import Counter
#from itertools import accumulate
# from itertools import groupby
# from itertools import permutations
# from itertools import combinations
# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse.csgraph import csgraph_from_dense
# from scipy.sparse.csgraph import dijkstra
# map(int,input().split())

class Dijkstra(object):
	"""
	ダイクストラ法（二分ヒープ）による最短経路探索
	計算量: O((E+V)logV)
	"""
	
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
		"""
		startノードからgoalノードまでの最短距離
		"""
		return self.dist[goal]
	
	def shortest_path(self, goal):
		"""
		startノードからgoalノードまでの最短経路
		"""
		path = []
		node = goal
		while node is not None:
			path.append(node)
			node = self.prev[node]
		return path[::-1]


class Graph(object):
	"""
	隣接リストによる有向グラフ
	"""
	
	def __init__(self):
		self.graph = defaultdict(list)
	
	def __len__(self):
		return len(self.graph)
	
	def add_edge(self, src, dst, weight=1):
		self.graph[src].append((dst, weight))
	
	def get_nodes(self):
		return self.graph.keys()


def main():
	N=int(input())
	
	G=Graph()
	
	for i in range(N-1):
		u,v,w=map(int,input().split())
		u-=1
		v-=1
		
		G.add_edge(u,v,w)
		G.add_edge(v,u,w)
	
	D=Dijkstra(G,0)
	
	for i in range(N):
		print(D.shortest_distance(i)%2)
	
	
	
	
if __name__ == "__main__":
	main()
