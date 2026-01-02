import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class SegmentTree(object):
	#N:処理する区間の長さ
	def __init__(self, N):
		self.N = N
		self.N0 = 2 ** (N - 1).bit_length()
		self.initVal = 0
		self.data = [self.initVal] * (2 * self.N0)

	# 区間クエリの種類
	def calc(self, a, b):
		return a + b

	# セグメント木の中身をリストAで初期化
	def initialize(self, A):
		for i in range(self.N):
			self.data[self.N0 - 1 + i] = A[i]
		for i in range(self.N0 - 2, -1, -1):
			self.data[i] = self.calc(self.data[2 * i + 1], self.data[2 * i + 2])

	#k番目の値をxに更新
	def update(self, k, x):
		k += self.N0 - 1
		self.data[k] = x
		while k > 0:
			k = (k - 1) // 2
			self.data[k] = self.calc(self.data[2 * k + 1], self.data[2 * k + 2])

	# k番目の値を取得
	def pointQuery(self, k):
		return self.data[k + self.N0 - 1]

	# k番目の値にxを加算
	def add(self, k, x):
		k += self.N0 - 1
		self.data[k] += x
		while k > 0:
			k = (k - 1) // 2
			self.data[k] = self.calc(self.data[2 * k + 1], self.data[2 * k + 2])

	#区間[l, r]の演算値
	def query(self, l, r):
		L = l + self.N0; R = r + self.N0 + 1
		m = self.initVal
		while L < R:
			if R & 1:
				R -= 1
				m = self.calc(m, self.data[R - 1])
			if L & 1:
				m = self.calc(m, self.data[L - 1])
				L += 1
			L >>= 1; R >>= 1

		return m

def main():
	N, Q = getlist()
	A = getlist()
	Seg = SegmentTree(N)
	Seg.initialize(A)
	for i in range(Q):
		q, a, b = getlist()
		if q == 0:
			Seg.add(a, b)
		else:
			res = Seg.query(a, b - 1)
			print(res)

if __name__ == '__main__':
	main()