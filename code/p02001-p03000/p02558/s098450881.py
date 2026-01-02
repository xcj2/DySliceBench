import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n + 1)]
		self.rank = [0] * (n + 1)
		self.size = [1] * (n + 1)

	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]

	def union(self, x, y):
		x = self.find(x); y = self.find(y)
		if x == y:
			return

		if self.rank[x] < self.rank[y]:
			self.size[y] += self.size[x]
			self.size[x] = 0
			self.par[x] = y
		else:
			self.size[x] += self.size[y]
			self.size[y] = 0
			self.par[y] = x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1

	def same_check(self, x, y):
		return self.find(x) == self.find(y)

	def getsize(self, x):
		x = self.find(x)
		return self.size[x]

def main():
	N, Q = getlist()
	UF = UnionFind(N)
	for i in range(Q):
		q, u, v = getlist()
		if q == 0:
			UF.union(u, v)
		else:
			if UF.same_check(u, v):
				print(1)
			else:
				print(0)

if __name__ == '__main__':
	main()