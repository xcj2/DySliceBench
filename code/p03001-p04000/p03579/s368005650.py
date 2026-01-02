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
	def __init__(self, graph, s, N):
		self.g = graph.graph
		self.Q = queue.Queue()
		self.Q.put(0)
		self.W = [INF] * N #sからの距離
		self.visit = ["No"] * N #見たか判定
		self.visit[s] = "Yes"
		self.W[s] = 0
		self.judge = "Yes"
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.W[i] = self.W[v] + 1
					self.Q.put(i)
					self.visit[i] = "Yes"
				#二部グラフ判定
				else:
					if (self.W[i] - self.W[v] - 1) % 2 == 1:
						self.judge = "No"
						break

#処理内容
def main():
	N, M = getlist()
	G = Graph()
	for i in range(M):
		a, b = getlist()
		G.add_edge(a - 1, b - 1)
		G.add_edge(b - 1, a - 1)
	BF = BFS(G, 0, N)
	if BF.judge == "No":
		print(int(N * (N - 1) // 2) - M)
	else:
		even = 0
		odd = 0
		for i in BF.W:
			if i % 2 == 0:
				even += 1
			else:
				odd += 1
		print(even * odd - M)

if __name__ == '__main__':
	main()