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
	r1, c1, r2, c2 = getlist()
	Com1 = Combination(r1 + c2 + 1, con)
	Com2 = Combination(r1 + c1, con)
	ans = 0
	val1 = Com1.com(r1 + c2 + 1, r1 + 1)
	val2 = Com2.com(r1 + c1, r1 + 1)
	ans += val1 - val2
	for R in range(r1, r2):
		inv = pow(R + 2, con - 2, con)
		val1 = (val1 * (R + c2 + 2) * inv) % con
		val2 = (val2 * (R + c1 + 1) * inv) % con
		ans += val1 - val2
		ans %= con
	
	ans %= con
	print(ans)
	 #mod conにおける逆元


	


if __name__ == '__main__':
	main()