# AOJ 0180 Demolition of Bridges
# Python3 2018.6.22

# UNION-FIND library
class UnionSet:
	def __init__(self, nmax):
		self.size = [1]*nmax
		self.id = [i for i in range(nmax+1)]
	def root(self, i):
		while i != self.id[i]:
			self.id[i] = self.id[self.id[i]]
			i = self.id[i]
		return i
	def connected(self, p, q): return self.root(p) == self.root(q)
	def unite(self, p, q):
		i, j = self.root(p), self.root(q)
		if i == j: return
		if self.size[i] < self.size[j]:
			self.id[i] = j
			self.size[j] += self.size[i]
		else:
			self.id[j] = i
			self.size[i] += self.size[j]
# UNION-FIND library

# 最小全域木。V:総ノード数、E:枝情報(a,b,cost)
def kruskal(V, edge):
	edge2 = sorted(edge, key=lambda x:(x[2]))
	u = UnionSet(V)
	ans = 0
	for e in edge2:
		if not u.connected(e[0], e[1]):
			u.unite(e[0], e[1])
			ans += e[2]
	return ans;

while 1:
	n, m = map(int, input().split())
	if n == 0: break
	edge = []
	for i in range(m):
		s, t, w = map(int, input().split())
		edge.append((s, t, w))
	print(kruskal(n, edge))
