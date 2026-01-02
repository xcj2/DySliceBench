import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
from collections import deque
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

def DFS(G, W, Wlist, visit, node):
	for i in G.graph[node]:
		if visit[i] == 0:
			visit[i] = 1
			DFS(G, W, Wlist, visit, i)
			W[node] += W[i]
			Wlist.append(W[i])

class BFS(object):
	def __init__(self, graph, s, N):
		self.g = graph.graph
		self.Q = deque(); self.Q.append(s)
		self.dist = [INF] * N; self.dist[s] = 0
		self.prev = [None] * N; self.prev[s] = -1
		self.order = []
		while self.Q:
			v = self.Q.popleft()
			self.order.append(v)
			for i in self.g[v]:
				if self.dist[i] == INF:
					self.dist[i] = self.dist[v] + 1
					self.prev[i] = v
					self.Q.append(i)


#処理内容
def main():
	#入力
	N = int(input())
	G = Graph()
	Nedge = [0] * N
	for i in range(N - 1):
		a, b = getlist()
		a -= 1; b -= 1
		G.add_edge(a, b)
		G.add_edge(b, a)
		Nedge[a] += 1; Nedge[b] += 1

	W = [1] * N
	#葉の場合の処理
	# for i in range(N):
	# 	if Nedge[i] == 1:
	# 		W[i] = 1

	BF = BFS(G, 0, N)

	for i in range(N - 1, 0, -1):
		v = BF.order[i]
		W[BF.prev[v]] += W[v]

	Wlist = []
	for i in range(N):
		for j in G.graph[i]:
			if j != BF.prev[i]:
				Wlist.append(W[j])
	for i in range(N):
		Wlist.append(N - W[i])

	pow2 = pow(2, N - 1, con)
	ans_up = N * (pow2 - 1)
	for i in Wlist:
		ans_up -= pow(2, i, con) - 1
		ans_up %= con

	ans = ans_up * pow(pow2 * 2, con - 2, con)
	print(ans % con)

if __name__ == '__main__':
	main()