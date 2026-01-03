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

def DFS(G, A, use, Wlist, visit, jud, node):
	for i in G.graph[node]:
		if visit[i] != "Yes":
			visit[i] = "Yes"
			DFS(G, A, use, Wlist, visit, jud, i)
			Wlist[node].append(use[i])

	#抜けの処理
	if Wlist[node] == []:
		use[node] = A[node]
	else:
		Z = sum(Wlist[node])
		if max(max(Wlist[node]), (Z + 1) // 2) <= A[node] and A[node] <= Z:
			use[node] = 2 * A[node] - Z
		else:
			use[node] = 2 * A[node] - Z
			jud[node] = "NO"

#処理内容
def main():
	N = int(input())
	A = getlist()
	G = Graph()
	for i in range(N - 1):
		a, b = getlist()
		a -= 1; b -= 1
		G.add_edge(a, b)
		G.add_edge(b, a)

	#面倒なケース
	if N == 2:
		if A[0] == A[1]:
			print("YES")
			return
		else:
			print("NO")
			return

	s = None
	for i in range(N):
		if len(G.graph[i]) >= 2:
			s = i
			break
	#DFS
	judge = "YES"
	use = [None] * N
	jud = ["YES"] * N
	Wlist = [[] for i in range(N)]
	visit = ["No"] * N
	visit[s] = "Yes"
	DFS(G, A, use, Wlist, visit, jud, s)
	# print(use)

	for i in range(N):
		if jud[i] == "NO":
			judge = "NO"

	if use[s] != 0:
		judge = "NO"
	#答え
	print(judge)

if __name__ == '__main__':
	main()