#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
import queue

#入力受け取り
def getlist():
	return list(map(int, input().split()))

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
	def __init__(self, graph, S, N):
		self.g = graph.graph
		self.Q = queue.Queue()
		self.dist = [INF] * N
		self.visit = ["No"] * N
		self.Q.put(S)
		self.dist[S] = 0
		self.visit[S] = "Yes"
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.dist[i] = self.dist[v] + 1
					self.Q.put(i)
					self.visit[i] = "Yes"

#処理内容
def main():
	#入力処理
	N, M = getlist()
	G = Graph()
	for i in range(M):
		u, v = getlist()
		G.add_edge(u - 1, v - 1 + N)
		G.add_edge(u - 1 + N, v - 1 + 2 * N)
		G.add_edge(u - 1 + 2 * N, v - 1)

	S, T = getlist()
	S -= 1
	T -= 1
	#BFS
	BF = BFS(G, S, 3 * N)
	D = BF.dist
	if D[T] == INF:
		print(-1)
	else:
		print(D[T] // 3)

if __name__ == '__main__':
	main()