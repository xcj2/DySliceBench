from collections import defaultdict
import queue

INF = float("inf")

def getlist():
	return list(map(int, input().split()))

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
		self.judge = "Yes"
		self.g = graph.graph
		self.Q = queue.Queue()
		self.dist = [INF] * N
		self.visit = ["No"] * N
		self.visit[s] = "Yes"
		self.dist[s] = 0
		self.Q.put(s)
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.dist[i] = self.dist[v] + 1
					self.Q.put(i)
					self.visit[i] = "Yes"
				else:
					if (self.dist[i] - self.dist[v]) % 2 == 0:
						self.judge = "No"

	def ans(self):
		return max(self.dist)

#処理内容
def main():
	#初期化
	N = int(input())
	L = []
	for i in range(N):
		S = list(input())
		L.append(S)
	G = Graph()
	for i in range(N):
		for j in range(i + 1, N):
			if L[i][j] == "1":
				G.add_edge(i, j)
				G.add_edge(j, i)
	#BFS
	jud = "Yes"
	A = - INF
	for i in range(N):
		bfs = BFS(G, i, N)
		A = max(bfs.ans(), A)
		if bfs.judge == "No":
			jud = "No"
	if jud == "No":
		print(-1)
	else:
		print(A + 1)

if __name__ == '__main__':
	main()