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

class BFS(object):
	def __init__(self, graph, s, N):
		self.g = graph.graph
		self.Q = deque(); self.Q.append(s)
		self.dist = [INF] * N; self.dist[s] = 0
		while self.Q:
			v = self.Q.popleft()
			for i in self.g[v]:
				if self.dist[i] == INF:
					self.dist[i] = self.dist[v] + 1
					self.Q.append(i)

#処理内容
def main():
	N = int(input())
	X = list(map(int, list(input())))

	G = Graph()
	for i in range(1, 2 * (10 ** 5) + 1):
		cnt1 = 0
		n = i
		while True:
			if n % 2 == 1:
				cnt1 += 1
			n = int(n // 2)
			if n == 0:
				break
		a = i % cnt1; b = i
		G.add_edge(a, b)

	BF = BFS(G, 0, 2 * (10 ** 5) + 1)
	dist = BF.dist

	X1cnt = 0
	for i in X:
		if i == 1:
			X1cnt += 1

	if X1cnt == 0:
		for i in range(N):
			print(1)

	elif X1cnt == 1:
		Xplus = 0
		for i in range(N):
			Xplus += pow(2, i, X1cnt + 1) * X[-1 - i]

		for i in range(N):
			if X[i] == 1:
				print(0)
			else:
				val = Xplus
				val += pow(2, N - 1 - i, X1cnt + 1)
				val %= X1cnt + 1
				print(dist[val] + 1)

	else:
		Xplus = 0
		Xnone = 0
		Xminus = 0
		for i in range(N):
			Xplus += pow(2, i, X1cnt + 1) * X[-1 - i]
			Xnone += pow(2, i, X1cnt) * X[-1 - i]
			Xminus += pow(2, i, X1cnt - 1) * X[-1 - i]

		Xplus %= X1cnt + 1
		Xnone %= X1cnt
		Xminus %= X1cnt - 1
		for i in range(N):
			if X[i] == 1:
				val = Xminus
				val -= pow(2, N - 1 - i, X1cnt - 1)
				val %= X1cnt - 1
				print(dist[val] + 1)
			else:
				val = Xplus
				val += pow(2, N - 1 - i, X1cnt + 1)
				val %= X1cnt + 1
				print(dist[val] + 1)


if __name__ == '__main__':
	main()