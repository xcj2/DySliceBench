#設定
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)

#ライブラリインポート
from collections import defaultdict

#入力受け取り
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

#val = 0

def DFS(G, anstenna, edge_num, have, visit, node):
	cnt = 0
	for i in G.graph[node]:
		if visit[i] != "Yes":
			visit[i] = "Yes"
			DFS(G, anstenna, edge_num, have, visit, i)
			if have[i] == 1:
				cnt += 1
				anstenna[node] += anstenna[i]

	if cnt < edge_num[node] - 1:
		anstenna[node] += edge_num[node] - 1 - cnt
	if anstenna[node] >= 1:
		have[node] = 1

#処理内容
def main():
	N = int(input())
	G = Graph()
	for i in range(N - 1):
		a, b = getlist()
		G.add_edge(a, b)
		G.add_edge(b, a)

	if N == 2:
		print(1)
		return

	#DFS
	anstenna = [0] * (N + 1)
	have = [0] * (N + 1)
	edge_num = [len(G.graph[i]) - 1 for i in range(N + 1)]

	if max(edge_num) <= 1:
		print(1)
		return

	visit = ["No"] * (N + 1)
	visit[N] = "Yes"
	s = None
	for i in range(N):
		if edge_num[i] >= 1:
			s = i
			break
	G.add_edge(N, s)
	G.add_edge(s, N)
	edge_num[s] += 1

	DFS(G, anstenna, edge_num, have, visit, N)
	ans = anstenna[N]
	if edge_num[s] == 2:
		cnt = 0
		for i in G.graph[s]:
			if have[i] == 1:
				cnt += 1
		if cnt <= 2:
			ans += 1

	print(ans)

if __name__ == '__main__':
	main()