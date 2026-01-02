import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

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
	N, M = getlist()
	ComM = Combination(M, con)
	ComN = Combination(N, con)
	anspre = (ComM.fac[M] * ComM.finv[M - N]) % con

	anspre2 = 0
	for i in range(N + 1):
		val = (ComN.com(N, i) * ComM.fac[M - i] * ComM.finv[M - N]) % con
		if i % 2 == 0:
			anspre2 += val
		else:
			anspre2 -= val

	ans = anspre * anspre2 % con
	print(ans)

if __name__ == '__main__':
	main()