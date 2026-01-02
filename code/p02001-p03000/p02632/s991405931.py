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
	K = int(input())
	S = list(input())
	N = len(S)
	C = Combination(N + K, con)
	ans = pow(26, K + N, con)
	for i in range(N):
		ans -= C.com(N + K, i) * pow(25, K + N - i, con)
		ans %= con

	print(ans)



if __name__ == '__main__':
	main()