#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
import queue
import copy

INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def Bellman_Ford(N, E, G, dist):
	for i in range(N):
		for a, b, w in G:
			if dist[b] > dist[a] + w:
				dist[b] = dist[a] + w

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
	N, M, P = getlist()
	dist = [INF] * N
	dist[0] = 0
	G = []
	D = Graph()
	Drev = Graph()
	for i in range(M):
		a, b, w = getlist()
		G.append([a - 1, b - 1, P - w])
		D.add_edge(a - 1, b - 1)
		Drev.add_edge(b - 1, a - 1)
	
	#BFS 0→N-1の経路判定
	BF = BFS(D, 0, N)
	BFrev = BFS(Drev, N - 1, N)
	check1 = BF.visit
	check2 = BFrev.visit
	judge = ["No"] * N
	for i in range(N):
		if check1[i] == "Yes" and check2[i] == "Yes":
			judge[i] = "Yes"

	#NM回、2NM回処理
	Bellman_Ford(N, M, G, dist)
	d1 = copy.copy(dist)
	Bellman_Ford(N, M, G, dist)
	d2 = dist

	#判定、出力

	judge_ans = "No"
	for i in range(N):
		if judge[i] == "Yes" and d1[i] != d2[i]:
			judge_ans = "Yes"
			break
	if judge_ans == "Yes":
		print(-1)
	else:
		print(max(-dist[-1] , 0))

if __name__ == '__main__':
	main()