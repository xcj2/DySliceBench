import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
import bisect
con = 998244353; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class SegmentTree(object):
	def __init__(self, N):
		self.N0 = 2 ** (N - 1).bit_length()
		self.data = [0] * (2 * self.N0)

	def update(self, k, x):
		k += self.N0 - 1
		self.data[k] = x
		while k > 0:
			k = (k - 1) // 2
			self.data[k] = max(self.data[2 * k + 1], self.data[2 * k + 2])

	def query(self, l, r):
		L = l + self.N0; R = r + self.N0 + 1
		m = 0
		while L < R:
			if R & 1:
				R -= 1
				m = max(m, self.data[R - 1])
			if L & 1:
				m = max(m, self.data[L - 1])
				L += 1
			L >>= 1; R >>= 1

		return m

#処理内容
def main():
	N = int(input())
	XD = [None] * N
	for i in range(N):
		X, D = getlist()
		XD[i] = [X, D]
	XD.sort()
	Xl = [XD[i][0] for i in range(N)]
	Xl.append(INF)

	Seg = SegmentTree(N)
	IND = [None] * N
	for i in range(N):
		ind = bisect.bisect_left(Xl, XD[i][0] + XD[i][1]) - 1
		Seg.update(i, ind)
		IND[i] = ind

	#DP初期化
	DP = [[0] for i in range(N + 1)]
	DP[N] = 1
	# print(Xl)
	# print(IND)

	for i in range(N - 1, -1, -1):
		ind = Seg.query(i, IND[i])
		Seg.update(i, ind)
		DP[i] = DP[i + 1] + DP[ind + 1]
		DP[i] %= con

	ans = DP[0]
	print(ans)

if __name__ == '__main__':
	main()