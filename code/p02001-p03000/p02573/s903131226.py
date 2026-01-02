import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mat = lambda x, y, v: [[v]*y for _ in range(x)]
ten = lambda x, y, z, v: [mat(y, z, v) for _ in range(x)]
mod = 1000000007
sys.setrecursionlimit(1000000)

class UnionFind:
	def __init__(self, n):
		self.n = n
		self.sizes = [0]*n
		self.parents = list(range(n))

	def find(self, x):
		while x != self.parents[x]:
			self.parents[x] = self.parents[self.parents[x]]
			x = self.parents[x]
		return self.parents[x]

	def unite(self, x, y):
		x, y = self.find(x), self.find(y)
		if x == y:
			return
		if self.sizes[x] < self.sizes[y]:
			x, y = y, x
		self.parents[y] = x
		self.sizes[x] += self.sizes[y]
	
	def add(self, x):
		self.sizes[x] = 1
		
	def size(self, x):
		return self.sizes[self.find(x)]

N, M = rl()
edges = set()
for i in range(M):
	a, b = rl()
	a, b = a-1, b-1
	edges.add((a,b))

uf =UnionFind(N)

for a, b in edges:
	uf.unite(a, b)
	uf.find(a)
	uf.find(b)

ans = 0
cnt = [0] * N
for i in range(N):
	p = uf.find(i)
	np = cnt[p] + 1
	ans = max(ans, np)
	cnt[p] = np
print(ans)
