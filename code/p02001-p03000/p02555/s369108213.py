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

	def fact(self, k):
		return self.facts[k] % mod

	def rfact(self, k):
		if k == 0: return 1
		return self.rfacts[k] % mod

S = ri()

n = S // 3

cm = CombMod(S)

def f(i, m):
	a = i-1 + m
	ret = cm.fact(a) * cm.rfact(i-1) * cm.rfact(m)
	return ret % mod

ans = 0
for i in range(1, n+1):
	m = S - i*3
	ans += f(i, m)
	ans %= mod
print(ans)
