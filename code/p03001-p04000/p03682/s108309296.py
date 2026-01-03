from operator import itemgetter as get

class UnionFind():
	def __init__(self, n):
		self.n = n
		self.root = [-1] * (n + 1)
		self.rank = [0] * (n + 1)

	def find(self, x):
		if self.root[x] < 0:
			return x
		else:
			self.root[x] = self.find(self.root[x])
			return self.root[x]

	def unite(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x == y:
			return 0
		elif self.rank[x] > self.rank[y]:
			self.root[x] += self.root[y]
			self.root[y] = x
		else:
			self.root[y] += self.root[x]
			self.root[x] = y
			if self.rank[x] == self.rank[y]:
				self.rank[y] += 1

	def isSame(self, x, y):
		return self.find(x) == self.find(y)

	def size(self, x):
		return -self.root[self.find(x)]


def main():
	n, *L = map(int, open(0).read().split())
	x_order = sorted([(x, y, i) for i, (x, y) in enumerate(zip(*[iter(L)] * 2))])
	con = []
	for p1, p2 in zip(x_order, x_order[1:]):
		con.append((p1[2], p2[2], min(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))))
	y_order = sorted(x_order, key=get(1))
	for p1, p2 in zip(y_order, y_order[1:]):
		con.append((p1[2], p2[2], min(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))))
	uf = UnionFind(n)
	ans = 0
	for i, j, c in sorted(con, key=get(2)):
		if uf.isSame(i, j):
			continue
		ans += c
		uf.unite(i, j)
	print(ans)


if __name__ == "__main__":
	main()
