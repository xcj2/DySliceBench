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

class CombMod:
	def __init__(self, N):
		facts = [1]
		rfacts = [1]
		for i in range(1, N+1):
			facts.append(facts[i-1]*i % mod)
			rfacts.append(pow(facts[i], mod-2, mod))
		self.facts = facts
		self.rfacts = rfacts

	def comb(self, n, k):
		return self.facts[n]*self.rfacts[k]*self.rfacts[n-k] % mod

	def perm(self, n, k):
		return self.facts[n]*self.rfacts[n-k] % mod

	def fact(self, n):
		return self.facts[n] % mod

	def rfact(self, n):
		return self.rfacts[n] % mod


N, K = rl()
cm = CombMod(N)
for i in range(1, K+1):
	remain = N-(K+i-1)
	if i-1 > N-K:
		print(0)
		continue
	cnt = cm.comb(K-1, i-1) * cm.comb(remain+i, remain)
	print(cnt % mod)

