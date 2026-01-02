INF = 2 ** 31 - 1
class SegmentTree:
	def __init__(self, n):
		self.N = 1
		while self.N < n:
			self.N *= 2
		self.tree = [INF] * (self.N * 2 - 1)

	# O(ln(n))
	def update(self, i, x):
		i += self.N - 1
		self.tree[i] = x
		while i > 0:
			i = (i-1) // 2
			self.tree[i] = min(self.tree[i*2+1], self.tree[i*2+2])

	def find(self, a, b, k, l, r):
		"""[a, b), ノードkが[l, r)を担当する"""
		if r <= a or b <= l:
			return INF
		if a <= l and r <= b:
			return self.tree[k]
		else:
			c1 = self.find(a, b, 2*k+1, l, (r+l)//2)
			c2 = self.find(a, b, 2*k+2, (l+r)//2, r)
			return min(c1, c2)

import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n, q = map(int, input().strip().split())
	st = SegmentTree(n)
	for _ in range(q):
		com, x, y = map(int, input().strip().split())
		if com:
			print(st.find(x, y+1, 0, 0, st.N))
		else:
			st.update(x, y)

if __name__ == '__main__':
	main()

