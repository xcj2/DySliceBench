import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 998244353; INF = float("inf")

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

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, M, K = getlist()
	if N == 1:
		print(M)
		return

	Com = Combination(N - 1, con)
	ans = 0
	for i in range(N - 1 - K, N):
		ans += Com.com(N - 1, i) * pow(M - 1, i, con)
		ans %= con
	ans *= M
	ans %= con
	print(ans)


if __name__ == '__main__':
	main()