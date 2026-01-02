#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
from heapq import heappop, heappush

con = 10 ** 9 + 7
INF = float('inf')

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
					heappush(self.Q, (alt, v))


#処理内容
def main():
	N, M, S = getlist()
	G = Graph()
	#グラフ構築
	for _ in range(M):
		U, V, A, B = getlist()
		for i in range(2500 - A + 1):
			G.add_edge(U * (10 ** 5) + 2500 - i, V * (10 ** 5) + 2500 - A - i, B)
			G.add_edge(V * (10 ** 5) + 2500 - i, U * (10 ** 5) + 2500 - A - i, B)

	for i in range(N):
		#i + 1が都市番号
		C, D = getlist()
		for j in range(2500):
			G.add_edge((i + 1) * (10 ** 5) + j, (i + 1) * (10 ** 5) + min(j + C, 2500), D)

	#ダイクストラ
	D = Dijkstra(G, 10 ** 5 + min(2500, S))

	for i in range(2, N + 1):
		ans = INF
		for j in range(2501):
			ans = min(D.dist[i * (10 ** 5) + j], ans)
		print(ans)
	




if __name__ == '__main__':
	main()