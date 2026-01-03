# unionfind
class Uf:
	def __init__(self, N):
		self.p = list(range(N))
		self.rank = [0] * N
		self.size = [1] * N
	#検索 ノード番号を受け取って一番上の親ノードの番号を帰す
	def root(self, x):
		if self.p[x] != x:
			self.p[x] = self.root(self.p[x])

		return self.p[x]
	#同じ集合に属するか判定
	def same(self, x, y):
		return self.root(x) == self.root(y)
	#併合
	def unite(self, x, y):
		# 根を探す
		u = self.root(x)
		v = self.root(y)

		if u == v: return

		#木の高さを比較し、低いほうから高いほうに辺を張る
		if self.rank[u] < self.rank[v]:
			self.p[u] = v
			self.size[v] += self.size[u]
			self.size[u] = 0
		else:
			self.p[v] = u
			self.size[u] += self.size[v]
			self.size[v] = 0
			#木の高さが同じなら片方を1増やす
			if self.rank[u] == self.rank[v]:
				self.rank[u] += 1
	#ノード番号を受け取って、そのノードが含まれている集合のサイズを返す
	def count(self, x):
		return self.size[self.root(x)]

from collections import Counter	
N, K, L = map(int, input().split())
uf_load = Uf(N)
uf_rail = Uf(N)

for i in range(K):
	p, q = map(int, input().split())
	p-=1
	q-=1
	uf_load.unite(p, q)
for _ in range(L):
	r, s = map(int, input().split())
	r-=1
	s-=1
	uf_rail.unite(r, s)

union_sets = [(uf_load.root(i), uf_rail.root(i)) for i in range(N)]
counts=Counter(union_sets)
ans = [counts[union_set] for union_set in union_sets]
print(*ans)