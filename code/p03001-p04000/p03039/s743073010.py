#設定
import sys
input = sys.stdin.buffer.readline

con = 10 ** 9 + 7
#ライブラリインポート
from collections import defaultdict

class Combination(object):
	def __init__(self, N, con):
		self.fac = [0] * (N + 1)
		self.inv = [0] * (N + 1)
		self.finv = [0] * (N + 1)
		self.fac[0], self.fac[1] = 1, 1
		self.inv[1] = 1
		self.finv[0], self.finv[1] = 1, 1

		# 前計算
		for i in range(2, N + 1):
			self.fac[i] = self.fac[i - 1] * i % con
			self.inv[i] = self.inv[con % i] * (con - (con // i)) % con
			self.finv[i] = self.finv[i - 1] * self.inv[i] % con

	def com(self, N, k):
		return (self.fac[N] * self.finv[k] * self.finv[N - k]) % con

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, M, K = getlist()
	C = Combination(N * M - 2, con)
	c = C.com(N * M - 2, K - 2)
	s = (N * (N + 1) * (N - 1)) // 6 * (M ** 2)
	t = (M * (M + 1) * (M - 1)) // 6 * (N ** 2)
	ans = c * (s + t)
	print(ans % con)

if __name__ == '__main__':
	main()