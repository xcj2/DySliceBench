#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
import queue

INF = float("inf")

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def __len__(self):
		return len(self.graph)

	def add_edge(self, a, b):
		self.graph[a].append(b)

	def get_nodes(self):
		return self.graph.keys()

class BFS(object):
	def __init__(self, graph, s, N):
		self.g = graph.graph
		self.Q = queue.Queue()
		self.Q.put(s)
		self.dist = [INF] * N
		self.dist[s] = 0
		self.visit = ["No"] * N
		self.visit[s] = "Yes"
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.dist[i] = self.dist[v] + 1
					self.Q.put(i)
					self.visit[i] = "Yes"

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, u, v = getlist()
	u -= 1; v -= 1
	G = Graph()
	for i in range(N - 1):
		A, B = getlist()
		A -= 1; B -= 1
		G.add_edge(A, B)
		G.add_edge(B, A)
	BF_taka = BFS(G, u, N)
	BF_ao = BFS(G, v, N)
	taka_dist = BF_taka.dist
	ao_dist = BF_ao.dist
	dis = 0

	for i in range(N):
		val = taka_dist[i]
		xval = ao_dist[i]
		if val < xval:
			dis = max(dis, xval)
	
	print(dis - 1)


if __name__ == '__main__':
	main()