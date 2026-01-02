#設定
import sys
input = sys.stdin.buffer.readline

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

#処理内容
def main():
	N = int(input())
	#1-Nの数を3で割った数の個数(あまり)
	a0 = int(N // 3)
	a1 = int((N + 2) // 3)
	a2 = int((N + 1) // 3)

	#グラフ構築
	G = Graph()
	for i in range(N - 1):
		a, b = getlist()
		a -= 1; b -= 1
		G.add_edge(a, b)
		G.add_edge(b, a)

	#偶奇で判断 可能性判定	
	BF = BFS(G, 0, N)
	dist = BF.dist
	dis_even = 0
	dis_odd = 0
	for i in range(N):
		if dist[i] % 2 == 0:
			dis_even += 1
		else:
			dis_odd += 1

	ans = [0] * N
	judge = "No"
	S = [(i + 1) * 3 for i in range(a0)] + [i * 3 + 1 for i in range(a1)] + [i * 3 + 2 for i in range(a2)]
	if a2 <= dis_odd and a1 <= dis_even:
		judge = "Yes"
		c1 = 0
		c2 = 0
		for i in range(N):
			if dist[i] % 2 != 0:
				if c1 < a2:
					ans[i] = c1 * 3 + 2
					c1 += 1
			else:
				if c2 < a1:
					ans[i] = c2 * 3 + 1
					c2 += 1

		cnt = 1
		for i in range(N):
			if ans[i] == 0:
				ans[i] = 3 * cnt
				cnt += 1

		print(" ".join(map(str, ans)))

	elif a1 <= dis_odd and a2 <= dis_even:
		judge = "Yes"
		c1 = 0
		c2 = 0
		for i in range(N):
			if dist[i] % 2 != 0:
				if c1 < a1:
					ans[i] = c1 * 3 + 2
					c1 += 1
			else:
				if c2 < a2:
					ans[i] = c2 * 3 + 1
					c2 += 1

		cnt = 1
		for i in range(N):
			if ans[i] == 0:
				ans[i] = 3 * cnt
				cnt += 1

		print(" ".join(map(str, ans)))

	elif dis_odd <= a0:
		cnt = 0
		for i in range(N):
			if dist[i] % 2 != 0:
				ans[i] = S[cnt]
				cnt += 1
		for i in range(N):
			if ans[i] == 0:
				ans[i] = S[cnt]
				cnt += 1

		print(" ".join(map(str, ans)))

	else:
		cnt = 0
		for i in range(N):
			if dist[i] % 2 == 0:
				ans[i] = S[cnt]
				cnt += 1
		for i in range(N):
			if ans[i] == 0:
				ans[i] = S[cnt]
				cnt += 1

		print(" ".join(map(str, ans)))
	

if __name__ == '__main__':
	main()