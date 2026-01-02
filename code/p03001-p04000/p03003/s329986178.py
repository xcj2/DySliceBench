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
		n, nums = self.n, self.nums
		s, p = 0, 0
		for i in range(n.bit_length(), -1, -1):
			np = p + (1<<i)
			if np <= n and s+nums[np] < x:
				s += nums[np]
				p = np
		return p

N, M = rl()
S = rl()
T = rl()

h = defaultdict(list)
for i, t in enumerate(T):
	h[t].append(i)
bit = BIT(M+1)
for i, s in enumerate(S):
	vals = []
	for j in h[s]:
		vals.append((j, bit.sum(j)+1))
	for j, v in vals:
		bit.add(j+1, v%mod)
print((bit.sum(M)+1)%mod)
