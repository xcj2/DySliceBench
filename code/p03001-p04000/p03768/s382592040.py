import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def __len__(self):
		return len(self.graph)

	def add_edge(self, a, b):
		self.graph[a].append(b)

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, M = getlist()
	G = Graph()
	for i in range(M):
		a, b = getlist()
		a -= 1; b -= 1
		G.add_edge(a, b)
		G.add_edge(b, a)

	DP = [[-1] * N for i in range(11)]
	Q_C = []
	Q = int(input())
	for i in range(Q):
		u, d, c = getlist()
		u -= 1
		Q_C.append(c)
		DP[10 - d][u] = i

	Q_C.append(0)

	#DP更新
	for i in range(10):
		for j in range(N):
			DP[i + 1][j] = max(DP[i + 1][j], DP[i][j])
			for k in G.graph[j]:
				DP[i + 1][k] = max(DP[i + 1][k], DP[i][j])
	
	for i in range(N):
		ind = DP[10][i]
		print(Q_C[ind])

if __name__ == '__main__':
	main()