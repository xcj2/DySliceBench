#設定
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)

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

def DFS(G, W, Wlist, visit, node):
	for i in G.graph[node]:
		if visit[i] != "Yes":
			visit[i] = "Yes"
			DFS(G, W, Wlist, visit, i)
			W[node] += W[i]
			Wlist[node].append(W[i])
	W[node] += 1

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
	G = Graph()
	for i in range(N - 1):
		a, b = getlist()
		a -= 1; b -= 1
		G.add_edge(a, b)
		G.add_edge(b, a)
	#例外処理
	if N == 2:
		print("Second")
		return

	judge = "Second"
	#DFS 判定
	#1回目
	W = [0] * N
	visit = ["No"] * N
	visit[0] = "Yes"
	Wlist = [[] for i in range(N)]
	DFS(G, W, Wlist, visit, 0)
	# print(Wlist)
	for i in range(N):
		cnt = 0
		jud = "Yes"
		for j in Wlist[i]:
			if j % 2 == 1:
				cnt += 1
		if cnt >= 2:
			judge = "First"
			break

	#2回目
	W = [0] * N
	visit = ["No"] * N
	visit[1] = "Yes"
	Wlist = [[] for i in range(N)]
	DFS(G, W, Wlist, visit, 1)
	for i in range(N):
		cnt = 0
		jud = "Yes"
		for j in Wlist[i]:
			if j % 2 == 1:
				cnt += 1
		if cnt >= 2:
			judge = "First"
			break

	#3回目
	W = [0] * N
	visit = ["No"] * N
	visit[2] = "Yes"
	Wlist = [[] for i in range(N)]
	DFS(G, W, Wlist, visit, 2)
	for i in range(N):
		cnt = 0
		jud = "Yes"
		for j in Wlist[i]:
			if j % 2 == 1:
				cnt += 1
		if cnt >= 2:
			judge = "First"
			break

	if N % 2 == 1:
		judge = "First"

	print(judge)

if __name__ == '__main__':
	main()