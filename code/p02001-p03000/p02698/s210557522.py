#設定
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

#ライブラリインポート
from collections import defaultdict
import bisect
INF = float("inf")

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

def Euler_tour(G, node, visit, DP, prev, ans, A):
	for i in G.graph[node]:
		if visit[i] != "Yes":
			visit[i] = "Yes"
			#LIS更新
			x = bisect.bisect_left(DP, A[i])
			prev.append([x, DP[x]])
			DP[x] = A[i]
			ans[i] = bisect.bisect_left(DP, INF)
			# print(DP, i)
			# print(prev)
			Euler_tour(G, i, visit, DP, prev, ans, A)

	#LIS戻す
	x, val = prev.pop()
	DP[x] = val

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

	#DFS初期化
	DP = [INF] * N
	DP[0] = A[0]
	prev = [[0, A[0]]]
	ans = [None] * N
	ans[0] = 1
	visit = ["No"] * N
	visit[0] = "Yes"
	Euler_tour(G, 0, visit, DP, prev, ans, A)
	for i in range(N):
		print(ans[i])


if __name__ == '__main__':
	main()