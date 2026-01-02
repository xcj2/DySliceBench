import sys
input = sys.stdin.readline

class UnionFind:
	def __init__(self, n):
		self.rank = [0] * n
		self.parent = [0] * n
		self.make(n)

	def make(self, n):
		for i in range(n):
			self.parent[i] = i

	def unite(self, x, y):
		xroot = self.findset(x)
		yroot = self.findset(y)
		if self.rank[xroot] < self.rank[yroot]:
			self.parent[xroot] = yroot
		elif self.rank[xroot] > self.rank[yroot]:
			self.parent[yroot] = xroot
		else:
			self.parent[xroot] = yroot
			self.rank[yroot] += 1
			node = y
			while True:
				self.rank[node] += 1
				if self.parent[node] == node:
					break
				node = self.parent[node]
			self.rank[y] += 1

	def findset(self, x):
		if self.parent[x] == x:
			return x
		else:
			root = self.findset(self.parent[x])
			self.parent[x] = root
			return root

def main():
	n, q = map(int, input().strip().split())
	uf = UnionFind(n)
	for i in range(q):
		com, x, y = map(int, input().strip().split())
		if com == 0:
			uf.unite(x, y)
		else:
			xroot = uf.findset(x)
			yroot = uf.findset(y)
			# print("xr: {} yr: {}".format(xroot, yroot))
			if xroot == yroot:
				print("1")
			else:
				print("0")

if __name__ == '__main__':
	main()

