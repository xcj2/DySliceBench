import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
import queue
con = 10 ** 9 + 7; INF = float("inf")

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def __len__(self):
		return len(self.graph)

	def add_edge(self, a, b):
		self.graph[a].append(b)

class BFS(object):
	def __init__(self, graph, s, N):
		self.g = graph.graph
		self.Q = queue.Queue()
		self.Q.put(s)
		self.visit = ["No"] * N
		self.visit[s] = "Yes"
		self.prev = [None] * N
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					self.prev[i] = v
					self.Q.put(i)
					self.visit[i] = "Yes"

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	G = Graph()
	D = defaultdict(int)
	for i in range(N - 1):
		a, b = sorted(getlist())
		a -= 1; b -= 1
		G.add_edge(a, b)
		G.add_edge(b, a)
		D[10000 * a + b] = i

	M = int(input())
	MbitTable = [0] * (N - 1)
	for i in range(M):
		u, v = getlist()
		u -= 1; v -= 1
		BF = BFS(G, u, N)
		prev = BF.prev
		node = v
		edge = []
		while prev[node] != None:
			a, b = sorted([node, prev[node]])
			edgenum = D[10000 * a + b]
			edge.append(edgenum)
			node = prev[node]

		for j in edge:
			MbitTable[j] += 2 ** i

	DP = [[0] * (2 ** M) for i in range(N)]
	DP[0][0] = 1
	for i in range(N - 1):
		for j in range(2 ** M):
			DP[i + 1][j] += DP[i][j]
			DP[i + 1][j | MbitTable[i]] += DP[i][j]

	print(DP[-1][-1])

if __name__ == '__main__':
	main()