#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

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

#処理内容
def main():
	N, K = getlist()
	if K >= N:
		Com = Combination(2 * N - 1, con)
		ans = Com.com(2 * N - 1, N)
		print(ans)

	else:
		Com1 = Combination(N, con)
		Com2 = Combination(N - 1, con)
		ans = 0
		for i in range(1, K + 1):
			ans += Com1.com(N, i) * Com2.com(N - 1, i)
			ans %= con
		ans = (ans + 1) % con
		print(ans)
	
if __name__ == '__main__':
	main()