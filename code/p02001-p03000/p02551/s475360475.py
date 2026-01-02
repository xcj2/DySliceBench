import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class lazySegTree(object):
	def __init__(self, N):
		self.N = N
		self.LV = (N - 1).bit_length()
		self.N0 = 2 ** self.LV
		self.data = [N - 1] * (2 * self.N0)
		self.lazy = [INF] * (2 * self.N0)

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
			if v == INF:
				continue
			self.lazy[2 * i - 1] = min(self.lazy[2 * i - 1], v)
			self.lazy[2 * i] = min(self.lazy[2 * i], v)
			self.data[2 * i - 1] = min(self.data[2 * i - 1], v)
			self.data[2 * i] = min(self.data[2 * i], v)
			self.lazy[i - 1] = INF

	def update(self, l, r, x):
		*ids, = self.gindex(l, r + 1)
		self.propagates(*ids)

		L = self.N0 + l; R = self.N0 + r + 1
		while L < R:
			if R & 1:
				R -= 1
				self.lazy[R - 1] = min(self.lazy[R - 1], x)
				self.data[R - 1] = min(self.data[R - 1], x)
			if L & 1:
				self.lazy[L - 1] = min(self.lazy[L - 1], x)
				self.data[L - 1] = min(self.data[L - 1], x)
				L += 1
			L >>= 1; R >>= 1
		for i in ids:
			self.data[i - 1] = min(self.data[2 * i - 1], self.data[2 * i])

	# k番目の値を取得
	def pointQuery(self, k):
		*ids, = self.gindex(k, k + 1)
		self.propagates(*ids)
		return self.data[k + self.N0 - 1]

	# デバッグ用
	def debug(self):
		ids = [i for i in range(self.N0, 0, -1)]
		self.propagates(*ids)
		print(self.data[self.N0 - 1:])

def main():
	N, Q = getlist()
	lSeg_low = lazySegTree(N + 1)
	lSeg_col = lazySegTree(N + 1)
	ans = (N - 2) ** 2
	for i in range(Q):
		n, x = getlist()
		if n == 1:
			itr = lSeg_col.pointQuery(x)
			ans -= itr - 2
			lSeg_low.update(2, itr - 1, x)
		else:
			itr = lSeg_low.pointQuery(x)
			ans -= itr - 2
			lSeg_col.update(2, itr - 1, x)
		# lSeg_low.debug()
		# lSeg_col.debug()
		# print(2, itr, x)
	print(ans)
	# print((N - 2) ** 2 - ans)


if __name__ == '__main__':
	main()