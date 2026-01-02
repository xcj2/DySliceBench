from itertools import combinations
class UnionFind():
	def __init__(self, size):
		self.table = [-1 for _ in range(size)]

	def find(self, x):
		while self.table[x] >= 0:
			x = self.table[x]
		return x

	def union(self, x, y):
		s1 = self.find(x)
		s2 = self.find(y)
		if s1 != s2:
			if self.table[s1] > self.table[s2]:
				self.table[s2] = s1
			elif self.table[s1] < self.table[s2]:
				self.table[s1] = s2
			else:
				self.table[s1] = s2
				self.table[s2] -= 1
		return

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

ans = 0
for i in range(m):
	if i == 0:
		new_edges = edges[1:]
	elif i == m - 1:
		new_edges = edges[:m - 1]
	else:
		new_edges = edges[:i] + edges[i + 1:]
	uf = UnionFind(n)
	for e in new_edges:
		uf.union(e[0] - 1, e[1] - 1)
	for a, b in combinations(range(n), r=2):
		if uf.find(a) != uf.find(b):
			ans += 1
			break

print(ans)