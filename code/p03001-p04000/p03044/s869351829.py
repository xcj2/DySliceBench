import sys
sys.setrecursionlimit(100**4)

class Edge():
	def __init__(self, v, w):
		self._v = v
		self._w = w
	def v(self):
		return self._v
	def w(self):
		return self._w

def dfs(v, g, colors, color = 0):
	colors[v] = color
	if not len(g[v]):
		return
	for nv in g[v]:
		if colors[nv.v()] != -1:
			continue
		nc = color if nv.w() % 2 == 0 else 1 - color
		dfs(nv.v(), g, colors, nc)

def resolve():
	n = int(input())
	colors = [-1]*n
	g = [list() for _ in range(n)]
	for _ in range(n-1):
		u, v, w = map(int, input().split())
		g[v-1].append(Edge(u-1, w))
		g[u-1].append(Edge(v-1, w))
	for i in range(n):
		if colors[i] != -1:
			continue
		dfs(i, g, colors)
	for c in colors:
		print(c)
resolve()