#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

con = 10 ** 9 + 7

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
	A = getlist()
	A = sorted(A)
	if K == 1:
		print(0)
		return
	if K == N:
		print(A[N - 1] - A[0])
		return

	invlist = [1] * N
	for i in range(K + 1, N):
		invlist[i] = (invlist[i - 1] * i * pow(i - K , con - 2, con)) % con

	
	C = Combination(N, con)
	mul = C.com(N, K)
	ans = 0
	for i in range(N - 1):
		dist = A[i + 1] - A[i]
		val = mul
		if i + 1 >= K:
			val -= invlist[i + 1]
		if N - 1 - i >= K:
			val -= invlist[N - 1 - i]
		ans += dist * val
		ans %= con
	print(ans)


if __name__ == '__main__':
	main()