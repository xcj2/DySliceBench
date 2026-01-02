#設定
import sys
input = sys.stdin.buffer.readline
INF = float("inf")

#ライブラリインポート
from collections import defaultdict
from heapq import heappop, heappush

#入力受け取り
def getlist():
	return list(map(int, input().split()))

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def __len__(self):
		return len(self.graph)

	def add_edge(self, a, b, w):
		self.graph[a].append((b, w))

	def get_nodes(self):
		return self.graph.keys()

class Dijkstra(object):
	def __init__(self, graph, s):
		self.g = graph.graph
		self.dist = defaultdict(lambda: INF)
		self.dist[s] = 0
		self.prev = defaultdict(lambda: None)
		self.Q = []
		heappush(self.Q, (self.dist[s], s))
		while self.Q:
			dist_u, u = heappop(self.Q)
			if self.dist[u] < dist_u:
				continue
			for v, w in self.g[u]:
				alt = dist_u + w
				if self.dist[v] > alt:
					self.dist[v] = alt
					self.prev[v] = u
					heappush(self.Q, (alt, v))

#処理内容
def main():
	N, M = getlist()
	G = Graph()
	for i in range(M):
		L, R, C = getlist()
		G.add_edge(L - 1, R - 1, C)
	for i in range(N - 1):
		G.add_edge(i + 1, i, 0)
	D = Dijkstra(G, 0)
	if D.dist[N - 1] == INF:
		print(-1)
	else:
		print(D.dist[N - 1])

if __name__ == '__main__':
	main()