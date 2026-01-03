import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

#val = 0

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def __len__(self):
		return len(self.graph)

	def add_edge(self, a, b):
		self.graph[a].append(b)

	def get_nodes(self):
		return self.graph.keys()

def DFS(G, W, node):
	cnt = 0
	child = []
	for i in G.graph[node]:
		DFS(G, W, i)
		child.append(W[i])
		cnt += 1

	child.sort()
	rev = [i for i in range(cnt, -1, -1)]
	weight = 0
	for i in range(cnt):
		weight = max(weight, rev[i] + child[i])

	W[node] = weight


def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	G = Graph()
	for i in range(N - 1):
		a = int(input()) - 1
		b = i + 1
		G.add_edge(a, b)

	# print(G.graph)

	#DFS
	W = [0] * N
	DFS(G, W, 0)

	print(W[0])



if __name__ == '__main__':
	main()