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

N = ri()
A = rl()

class SegTree:
	def __init__(self, n, f=min, v=float('inf')):
		self.n = n
		self.f = f
		self.v = v
		self.nums = [v] * (2*n)
		
	def init(self, seq):
		n, f, nums = self.n, self.f, self.nums
		assert len(seq) == n, 'seq size error'
		for i, x in enumerate(seq):
			nums[i+n] = x
		for i in range(n-1, 0, -1):
			nums[i] = f(nums[i<<1], nums[i<<1|1])

	def update(self, i, x):
		n, f, nums = self.n, self.f, self.nums
		i += n
		nums[i] = x
		while i > 1:
			i >>= 1
			nums[i] = f(nums[i<<1], nums[i<<1|1]) # f(nums[i//2], nums[i//2+1])
	
	def query(self, l, r): # f([l, r))
		n, f, v, nums = self.n, self.f, self.v, self.nums
		l, r = l+n, r+n
		vl, vr = v, v
		while l < r:
			if l & 1:
				vl = f(vl, nums[l])
				l += 1
			if r & 1:
				r -= 1
				vr = f(nums[r], vr)
			l, r = l>>1, r>>1
		return f(vl, vr)

def gcd(a, b):
	return gcd(b, a%b) if b else a

st = SegTree(N, f=gcd, v=0)
st.init(A)

ans = -1
for i in range(N):
	g = gcd(st.query(0, i), st.query(i+1, N))
	ans = max(g, ans)
print(ans)

