class UnionFind():
	def __init__(self, n):
		self.n = n
		self.root = [-1]*(n+1)
		self.rank = [0]*(n+1)

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
		return self.find(x) == self.find(y) or x==y
		
def solve():
	n,_,*l=map(int,open(0).read().split())
	p=l[:n];xy=l[n:]
	ids=[0]*(n+1)
	for i,x in enumerate(p):ids[x]=i+1
	uf=UnionFind(n)
	for x,y in zip(*[iter(xy)]*2):uf.unite(x,y)
	print(sum(uf.isSame(i,ids[i])for i in range(1,n+1)))
	
if __name__=="__main__":solve()