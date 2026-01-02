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

mod = 998244353

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

N, K = rl()
lr = []
for i in range(K):
	l, r = rl()
	lr.append((l,r))

bit = BIT(N+1)
bit.add(1, 1)
bit.add(2, -1)

ans = 0
for i in range(1, N+1):
	s = bit.sum(i)
	s %= mod
	#print('s', s)
	for k in range(K):
		l, r = lr[k]
		if i+l <= N:
			#print('l', i+l, s)
			bit.add(i+l, s)
			if i+r+1 <= N:
				#print('r', i+r+1, -s)
				bit.add(i+r+1, -s)
			else:
				ans += s
				ans %= mod
print(ans)
#print(bit.sum(N) % mod)
