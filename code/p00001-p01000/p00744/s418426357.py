# https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
import sys
def input():
	return sys.stdin.readline()[:-1]
from math import gcd
from collections import deque
class Dinic:
	def __init__(self, n):
		self.n = n
		self.g = [[] for i in range(n)]

	def add_edge(self, fr, to, cap):
		#[to, cap, rev]
		forward = [to, cap, None]
		forward[2] = backward = [fr, 0, forward]
		self.g[fr].append(forward)
		self.g[to].append(backward)

	def add_bidirectional_edge(self, v1, v2, cap1, cap2):
		edge1 = [v2, cap1, None]
		edge1[2] = edge2 = [v1, cap2, edge1]
		self.g[v1].append(edge1)
		self.g[v2].append(edge2)

	def bfs(self, s, t):
		self.level = level = [None]*self.n
		deq = deque([s])
		level[s] = 0
		g = self.g
		while deq:
			v = deq.popleft()
			lv = level[v] + 1
			for w, cap, _ in g[v]:
				if cap and level[w] is None:
					level[w] = lv
					deq.append(w)
		return level[t] is not None

	def dfs(self, v, t, f):
		if v == t:
			return f
		level = self.level
		for e in self.it[v]:
			w, cap, rev = e
			if cap and level[v] < level[w]:
				d = self.dfs(w, t, min(f, cap))
				if d:
					e[1] -= d
					rev[1] += d
					return d
		return 0

	def flow(self, s, t):
		flow = 0
		INF = 10**30
		g = self.g
		while self.bfs(s, t):
			#*self.it, = map(iter, self.g)
			self.it = list(map(iter, self.g))
			f = INF
			while f:
				f = self.dfs(s, t, INF)
				flow += f
		return flow

while True:
	n, m = map(int, input().split())
	if n == 0:
		break
	b = []
	r = []
	while len(b) < n:
		b += list(map(int, input().split()))
	while len(r) < m:
		r += list(map(int, input().split()))
	dinic = Dinic(n+m+2)
	for i, x in enumerate(b):
		dinic.add_edge(n+m, i, 1)
		for j, y in enumerate(r):
			if gcd(x, y) > 1:
				dinic.add_edge(i, n+j, 1)
	for j in range(m):
		dinic.add_edge(n+j, n+m+1, 1)
	print(dinic.flow(n+m, n+m+1))

