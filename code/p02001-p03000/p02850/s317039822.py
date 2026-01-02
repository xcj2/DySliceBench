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
		self.Q.put(s)
		self.color = defaultdict(int)
		self.precolor = [None] * N
		self.visit = ["No"] * N
		self.visit[s] = "Yes"
		while not self.Q.empty():
			v = self.Q.get()
			self.c = 0
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.c += 1
					if self.c == self.precolor[v]:
						self.c += 1
					x, y = sorted([i, v])
					self.color[100000 * x + y] = self.c
					self.precolor[i] = self.c
					self.Q.put(i)
					self.visit[i] = "Yes"


#処理内容
def main():
	N = int(input())
	G = Graph()
	S = []
	for i in range(N - 1):
		a, b = getlist()
		a, b = sorted([a, b])
		G.add_edge(a - 1, b - 1)
		G.add_edge(b - 1, a - 1)
		S.append([a - 1, b - 1])
	BF = BFS(G, 0, N)
	D = BF.color
	#print(D)
	ans = []
	d = defaultdict(int)
	for i in range(N - 1):
		a = S[i][0]
		b = S[i][1]
		ans.append(D[100000 * a + b])
		d[D[100000 * a + b]] += 1
	print(len(d))
	for i in range(N - 1):
		print(ans[i])

if __name__ == '__main__':
	main()