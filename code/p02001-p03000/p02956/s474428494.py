import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
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
			self.data[k] = self.data[2 * k + 1] + self.data[2 * k + 2]

	def query(self, l, r):
		L = l + self.N0; R = r + self.N0 + 1
		m = 0
		while L < R:
			if R & 1:
				R -= 1
				m += self.data[R - 1]
			if L & 1:
				m += self.data[L - 1]
				L += 1
			L >>= 1; R >>= 1

		return m

#処理内容
def main():
	N = int(input())
	XY = [None] * N
	X = [None] * N
	Y = [None] * N
	for i in range(N):
		x, y = getlist()
		XY[i] = [x, y]
		X[i] = x; Y[i] = y

	#座圧
	X.sort(); Y.sort()
	Dx = defaultdict(int)
	Dy = defaultdict(int)
	for i in range(N):
		Dx[X[i]] = i
		Dy[Y[i]] = i

	for i in range(N):
		XY[i] = Dx[XY[i][0]], Dy[XY[i][1]]

	XY.sort(key=lambda x: x[0])
	YY = [XY[i][1] for i in range(N)]
	# print(YY)
	# print(XY)
	
	Segleft = SegmentTree(N)
	Segright = SegmentTree(N)

	#関係なく決まっている値
	ans = pow(2, N - 1, con) * N
	ans %= con

	yLU = [0] * N
	yLD = [0] * N
	yRU = [0] * N
	yRD = [0] * N

	#左初期化
	Segleft.update(YY[0], 1)

	for i in range(1, N - 1):
		y = YY[i]
		yLD[i] = Segleft.query(0, y)
		yLU[i] = Segleft.query(y, N - 1)
		Segleft.update(y, 1)

	#右初期化
	Segright.update(YY[N - 1], 1)

	for i in range(N - 2, 0, -1):
		y = YY[i]
		yRD[i] = Segright.query(0, y)
		yRU[i] = Segright.query(y, N - 1)
		Segright.update(y, 1)

	# print(yLD)
	# print(yLU)
	# print(yRD)
	# print(yRU)

	for i in range(1, N - 1):
		lu = yLU[i]; ru = yRU[i]
		ld = yLD[i]; rd = yRD[i]
		a = pow(2, lu, con)
		b = pow(2, ru, con)
		c = pow(2, ld, con)
		d = pow(2, rd, con)
		if rd != 0 and lu != 0:
			ans += (d - 1) * (a - 1) * b * c
		if ld != 0 and ru != 0:
			ans += (c - 1) * (b - 1) * a * d
		#包除
		if rd != 0 and lu != 0 and ld != 0 and ru != 0:
			ans -= (a - 1) * (b - 1) * (c - 1) * (d - 1)
		ans %= con

	print(ans)

if __name__ == '__main__':
	main()