import sys

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
	input = sys.stdin.buffer.readline
	n, m = map(int, input().split())
	lang = [[] for _ in range(m)]
	uf = UnionFind(n)
	for i in range(n):
		k, *ls = map(int, input().split())
		for l in ls:
			lang[l - 1].append(i)
	for speakers in lang:
		for x, y in zip(speakers, speakers[1:]):
			uf.unite(x, y)
	print("YES" if uf.size(0) == n else "NO")

if __name__=="__main__":
	main()