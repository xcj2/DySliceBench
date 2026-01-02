import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
import queue
con = 10 ** 9 + 7; INF = float("inf")

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
		self.g = graph.graph
		self.Q = queue.Queue()
		self.Q.put(s)
		self.dist = [INF] * N
		self.dist[s] = 0
		self.visit = ["No"] * N
		self.visit[s] = "Yes"
		self.prev = [None] * N
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.dist[i] = self.dist[v] + 1
					self.prev[i] = v
					self.Q.put(i)
					self.visit[i] = "Yes"

#処理内容
def main():
	N, M = getlist()
	G = Graph()
	for i in range(M):
		A, B = getlist()
		A -= 1; B -= 1
		G.add_edge(A, B)
		G.add_edge(B, A)

	BF = BFS(G, 0, N)
	print("Yes")
	prev = BF.prev
	for i in range(1, N):
		print(prev[i] + 1)

if __name__ == '__main__':
	main()