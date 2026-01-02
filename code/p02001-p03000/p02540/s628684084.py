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

class BIT:
	def __init__(self, n):
		self.n = n
		self.nums = [0] * (n+1)
		
	def add(self, i, x):
		n, nums = self.n, self.nums
		i += 1
		while i <= n:
			nums[i] += x
			i += i & -i
	
	def sum(self, i):
		nums = self.nums
		s = 0
		i += 1
		while i:
			s += nums[i]
			i -= i & -i
		return s
	
	def search(self, x):
		# minimum index i such that x <= self.sum(i)
		n, nums = self.n, self.nums
		s, p = 0, 0
		for i in range(n.bit_length(), -1, -1):
			np = p + (1<<i)
			if np <= n and s+nums[np] < x:
				s += nums[np]
				p = np
		return p

	def lowerbound(self, x):
		# minimum index i such that x <= i and i-th element
		return self.search(self.sum(x-1)+1)

	def upperbound(self, x):
		# minimum index i such that self.x < sum(i)
		return self.search(self.sum(x)+1)


class MultiSet:
	def __init__(self, n):
		self.bit = BIT(n)

	def insert(self, key):
		self.bit.add(key, 1)

	def erase(self, key):
		self.bit.add(key, -1)

	def top(self, i=0):
		# i-th smallest element
		return self.bit.search(i+1)

	def size(self):
		return self.bit.sum(self.bit.n-1)

	def count(self, key):
		# number of keys
		return self.bit.sum(key)-self.bit.sum(key-1)

	def lower_bound(self, key):
		# minimum key k no less than key (key <= k)
		return self.bit.search(self.bit.sum(key-1)+1)

	def upper_bound(self, key):
		# minimum key k greater than key (key < k)
		return self.bit.search(self.bit.sum(key)+1)

	def left_bound(self, key):
		s = self.bit.sum(key)
		if s <= 1: return -1
		return self.bit.search(s-1)

	def right_bound(self, key):
		s = self.bit.sum(key)
		if s == self.bit.n:
			return self.bit.n
		return self.bit.search(s+1)

	def debug(self):
		vals = []
		for i in range(self.bit.n):
			key = self.top(i)
			if key == self.bit.n: break
			vals.append(key)
		print(vals)

class UnionFind:
	# uf = UnionFind(N)
	# for x, y in pairs: uf.unite(x, y)
	# ans = max([uf.size(i) for i in range(N)])
	def __init__(self, n):
		self.n = n
		self.sizes = [1]*n
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

	def size(self, x):
		return self.sizes[self.find(x)]

N = ri()
x2y = [0] * N
y2x = [0] * N
i2x = [0] * N
x2i = [0] * N
y2i = [0] * N
for i in range(N):
	x, y = rl()
	x, y = x-1, y-1
	i2x[i] = x
	x2i[x] = i
	y2i[y] = i
	x2y[x] = y
	y2x[y] = x

uf = UnionFind(N)
ms = MultiSet(N)
for x in range(N):
	y = x2y[x]
	ms.insert(y)
	idx = ms.left_bound(y)
	while idx < N and idx >= 0:
		uf.unite(y2i[y], y2i[idx])
		ms.erase(y)
		y = idx
		idx = ms.left_bound(idx)

ms = MultiSet(N)
for x in reversed(range(N)):
	y = x2y[x]
	ms.insert(y)
	idx = ms.right_bound(y)
	while idx < N and idx >= 0:
		p = uf.find(idx)
		uf.unite(y2i[y], y2i[idx])
		ms.erase(y)
		y = idx
		idx = ms.right_bound(idx)

for i in range(N):
	print(uf.size(i))









