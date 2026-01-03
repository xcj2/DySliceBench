import copy

class UnionFind:
	def __init__(self, N):
		self._parent = [i for i in range(N)]

	def find(self, x):
		if self._parent[x] == x:
			return x
		else:
			return self.find(self._parent[x])

	def unite(self, a, b):
		ta = self.find(a)
		tb = self.find(b)
		if(ta != tb):
			self._parent[ta] = min(ta,tb)
			self._parent[tb] = self._parent[ta]
		
			
	def check(self, a, b):
		return self.find(a) == self.find(b)
		
if __name__ == '__main__':
	N,K,L = map(int, input().split())
	uf1 = UnionFind(N)
	for _ in range(K):
		p,q = map(int, input().split())
		uf1.unite(p-1,q-1)
	uf2 = UnionFind(N)
	for _ in range(L):
		s,r = map(int, input().split())
		uf2.unite(s-1,r-1)
	from collections import defaultdict
	d = defaultdict(int)
	for i in range(N):
		d[(uf1.find(i), uf2.find(i))] += 1
	ans = []
	for i in range(N):
		ans.append( str(d[(uf1.find(i), uf2.find(i))]) )
	print(' '.join(ans))