import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 998244353; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def inverse(N, mod):
	return (pow(N, mod - 2, mod))

class lazySegTree(object):
	def __init__(self, N):
		self.N = N
		self.LV = (N - 1).bit_length()
		self.N0 = 2 ** self.LV
		self.data = [0] * (2 * self.N0)
		self.lazy = [0] * (2 * self.N0)
		self.size = [1] * (2 * self.N0)
		for i in range(self.N):
			self.size[self.N0 - 1 + i] = pow(10, self.N - i - 1 , mod)
		for i in range(self.N0 - 2, -1, -1):
			self.size[i] = (self.size[2 * i + 1] + self.size[2 * i + 2]) % mod

	# 遅延セグ木の初期化
	def initialize(self):
		for i in range(self.N):
			self.data[self.N0 - 1 + i] = pow(10, self.N - i - 1, mod)
		for i in range(self.N0 - 2, -1, -1):
			self.data[i] = (self.data[2 * i + 1] + self.data[2 * i + 2]) % mod

	# 遅延伝播を行うindexを生成
	def gindex(self, l, r):
		L = (l + self.N0) >> 1; R = (r + self.N0) >> 1
		lc = 0 if l & 1 else (L & -L).bit_length()
		rc = 0 if r & 1 else (R & -R).bit_length()
		for i in range(self.LV):
			if rc <= i:
				yield R
			if L < R and lc <= i:
				yield L
			L >>= 1; R >>= 1

	# 遅延伝搬処理
	def propagates(self, *ids):
		for i in reversed(ids):
			v = self.lazy[i - 1]
			if not v:
				continue
			self.lazy[2 * i - 1] = v; self.lazy[2 * i] = v
			self.data[2 * i - 1] = v * self.size[2 * i - 1]
			self.data[2 * i] = v * self.size[2 * i]
			self.lazy[i - 1] = 0

	def update(self, l, r, x):
		*ids, = self.gindex(l, r + 1)
		self.propagates(*ids)

		L = self.N0 + l; R = self.N0 + r + 1
		while L < R:
			if R & 1:
				R -= 1
				self.lazy[R - 1] = x; self.data[R - 1] = x * self.size[R - 1]
			if L & 1:
				self.lazy[L - 1] = x; self.data[L - 1] = x * self.size[L - 1]
				L += 1
			L >>= 1; R >>= 1
		for i in ids:
			self.data[i - 1] = (self.data[2 * i - 1] + self.data[2 * i]) % mod

	# 区間[l, r]内の和を求める
	def query(self, l, r):
		self.propagates(*self.gindex(l, r + 1))
		L = self.N0 + l; R = self.N0 + r + 1
		s = 0
		while L < R:
			if R & 1:
				R -= 1
				s += self.data[R - 1]
			if L & 1:
				s += self.data[L - 1]
				L += 1
			L >>= 1; R >>= 1
			s %= mod
		return s

	# デバッグ用
	def debug(self):
		ids = [i for i in range(self.N0 - 1, 0, -1)]
		self.propagates(*ids)
		print(self.data[self.N0 - 1:])

def main():
	N, Q = getlist()
	lSeg = lazySegTree(N)
	lSeg.initialize()
	# lSeg.debug()
	for i in range(Q):
		L, R, D = getlist()
		L -= 1; R -= 1
		lSeg.update(L, R, D)
		ans = lSeg.query(0, N - 1)
		print(ans)





if __name__ == '__main__':
	main()