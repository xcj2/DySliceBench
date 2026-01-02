import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

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

#処理内容
def main():
	N, Q = getlist()
	c = getlist()
	LR = []
	lastappeared = [None] * N

	ans = [0] * Q
	for i in range(Q):
		l, r = getlist()
		l -= 1; r -= 1
		LR.append([r, l, i])

	LR.sort(key = lambda x:x[0])
	Seg = SegmentTree(N)
	right = 0
	for r, l, i in LR:
		while right <= r:
			itr = c[right] - 1
			if lastappeared[itr] == None:
				Seg.update(right, 1)
			else:
				Seg.update(lastappeared[itr], 0)
				Seg.update(right, 1)
			lastappeared[itr] = right
			right += 1

		if l == 0:
			anspre = Seg.query(0, r)
		else:
			anspre = Seg.query(l, r)
		ans[i] = anspre

	for i in range(Q):
		print(ans[i])



if __name__ == '__main__':
	main()