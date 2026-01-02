import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class Combination(object):
	def __init__(self, N, mod = 10 ** 9 + 7):
		self.fac = [0] * (N + 1)
		self.inv = [0] * (N + 1)
		self.finv = [0] * (N + 1)
		self.fac[0], self.fac[1] = 1, 1
		self.inv[1] = 1
		self.finv[0], self.finv[1] = 1, 1
		self.mod = mod

		# 前計算
		for i in range(2, N + 1):
			self.fac[i] = self.fac[i - 1] * i % mod
			self.inv[i] = self.inv[mod % i] * (mod - (mod // i)) % mod
			self.finv[i] = self.finv[i - 1] * self.inv[i] % mod

	def cmb(self, N, k):
		return (self.fac[N] * self.finv[k] * self.finv[N - k]) % self.mod

def main():
	S = int(input())
	ans = 0
	C = Combination(S)
	for i in range(1, S + 1):
		n = S - 3 * i; k = i - 1
		if n >= 0:
			ans += C.cmb(S - 2 * i - 1, i - 1)
			ans %= mod
		else:
			break

	print(ans)


if __name__ == '__main__':
	main()