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
		return - self.root[self.find(x)]

import sys
input = sys.stdin.buffer.readline
from collections import Counter
n,k,l=map(int,input().split())
uf1=UnionFind(n)
uf2=UnionFind(n)
for _ in range(k):
	uf1.unite(*map(int,input().split()))
for _ in range(l):
	uf2.unite(*map(int,input().split()))
ps=[(uf1.find(i),uf2.find(i)) for i in range(1,n+1)]
C=Counter(ps)
ans=[]
for i in range(n):
	if ps[i][0]<0 or ps[i][1]<0:
		ans.append(0)
	else:
		ans.append(C[ps[i]])
print(*ans)