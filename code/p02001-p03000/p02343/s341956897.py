class UnionFind():
	def __init__(self, n):
		self.n = n
		self.root = [-1]*(n+1)
		self.rank = [0]*(n+1)

	def find(self, x):
		if(self.root[x] < 0):
			return x
		else:
			self.root[x] = self.find(self.root[x])
			return self.root[x]
			
	def unite(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if(x == y):
			return 0
		elif(self.rank[x] > self.rank[y]):
			self.root[x] += self.root[y]
			self.root[y] = x
		else:
			self.root[y] += self.root[x]
			self.root[x] = y
			if(self.rank[x] == self.rank[y]):
				self.rank[y] += 1

	def isSame(self, x, y):
		return self.find(x) == self.find(y)

	def size(self, x):
		return -self.root[self.find(x)]

def solve():
	n,q,*l = map(int,open(0).read().split())
	uf = UnionFind(n)
	for c,x,y in zip(*[iter(l)]*3):
		if c:
			print(0 + uf.isSame(x,y))
		else:
			uf.unite(x,y)
            
if __name__=="__main__":
	solve()
