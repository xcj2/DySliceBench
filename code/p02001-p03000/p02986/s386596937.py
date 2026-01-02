import sys
from bisect import bisect
sys.setrecursionlimit(10**6)
def input():
	return sys.stdin.buffer.readline()[:-1]

class LCA():
	def __init__(self, adj_given, root_given):
		self.adj = adj = adj_given
		self.root = root_given
		self.n = n = len(adj)
		self.maxlog = 0
		while (1 << self.maxlog) < n:
			self.maxlog += 1
		maxlog = self.maxlog
		self.par = [[-1 for _ in range(n)] for _ in range(maxlog)]
		self.dep = [0 for _ in range(n)]
		self.num_key = [[0] for _ in range(n)]
		self.num_value = [[0] for _ in range(n)]
		self.sum_value = [[0] for _ in range(n)]
		self.first = [10**6 for _ in range(n)]
		self.first[self.root] = 0
		self.visited = 1
		self.cnt = 1
		self.dist = [0 for _ in range(n)]

	def dfs(self, x, pa, de, co, le):
		par = self.par
		dep = self.dep
		root = self.root
		
		par[0][x] = pa
		dep[x] = de

		if x != root and self.visited < n:
			self.num_key[co].append(self.cnt)
			self.num_value[co].append(self.num_value[co][-1] + 1)
			self.sum_value[co].append(self.sum_value[co][-1] + le)
			if self.first[x] == 10**6:
				self.visited += 1
				self.first[x] = self.cnt
			self.cnt += 1
			self.dist[x] = self.dist[pa] + le

		for v, c, l in adj[x]:
			if v != pa:
				self.dfs(v, x, de+1, c, l)

		if x != root and self.visited < n:
			self.num_key[co].append(self.cnt)
			self.num_value[co].append(self.num_value[co][-1] - 1)
			self.sum_value[co].append(self.sum_value[co][-1] - le)
			self.cnt += 1

		return

	def calc(self):
		root = self.root
		par = self.par
		maxlog = self.maxlog
		self.dfs(root, -1, 0, -1, 0)

		for k in range(maxlog-1):
			for v in range(n):
				if par[k][v] < 0:
					continue
				else:
					par[k+1][v] = par[k][par[k][v]]
		return

	def get_lca(self, u, v):
		par = self.par
		dep = self.dep
		maxlog = self.maxlog
		if dep[u] > dep[v]:
			u, v = v, u
		for k in range(maxlog):
			if ((dep[v] - dep[u]) >> k) & 1:
				v = par[k][v]

		if u == v:
			return u
		else:
			for k in range(maxlog-1, -1, -1):
				if par[k][u] != par[k][v]:
					u = par[k][u]
					v = par[k][v]
			return par[0][u]

n, q = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(n-1):
	a, b, c, d = map(int, input().split())
	adj[a-1].append((b-1, c-1, d))
	adj[b-1].append((a-1, c-1, d))

lca = LCA(adj, 0)
lca.calc()

for _ in range(q):
	x, y, u, v = map(int, input().split())
	x, u, v = x-1, u-1, v-1
	a = lca.get_lca(u, v)
	id_u = max(bisect(lca.num_key[x], lca.first[u])-1, 0)
	id_v = max(bisect(lca.num_key[x], lca.first[v])-1, 0)
	id_a = max(bisect(lca.num_key[x], lca.first[a])-1, 0)

	dist_u = lca.dist[u] + lca.num_value[x][id_u] * y - lca.sum_value[x][id_u]
	dist_v = lca.dist[v] + lca.num_value[x][id_v] * y - lca.sum_value[x][id_v]
	dist_a = lca.dist[a] + lca.num_value[x][id_a] * y - lca.sum_value[x][id_a]
	print(dist_u + dist_v - 2 * dist_a)