import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class SegmentTree(object):
	def __init__(self, N):
		self.N = N
		self.N0 = 2 ** (N - 1).bit_length()
		self.initVal = 0
		self.data = [self.initVal] * (2 * self.N0)

	# 区間クエリの種類
	def calc(self, a, b):
		return max(a, b)

	#k番目の値をxに更新
	def update(self, k, x):
		k += self.N0 - 1
		self.data[k] = x
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
	N, K = getlist()
	n = 3 * (10 ** 5) + 2
	Seg = SegmentTree(n)
	for i in range(N):
		a = int(input())
		l = max(0, a - K)
		r = min(n - 1, a + K)
		res = Seg.query(l, r)
		Seg.update(a, res + 1)

	ans = Seg.query(0, n - 1)
	print(ans)




if __name__ == '__main__':
	main()