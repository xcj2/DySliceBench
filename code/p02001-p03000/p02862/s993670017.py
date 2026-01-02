con = 10 ** 9 + 7
#ライブラリインポート
from collections import defaultdict

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

	def com(self, k, N):
		return (self.fac[N] * self.finv[k] * self.finv[N - k]) % con

#処理内容
def main():
	X, Y = getlist()
	N = (X + Y) // 3
	if (X + Y) % 3 != 0:
		print(0)
	elif X < N or Y < N:
		print(0)
	else:
		C = Combination(N, con)
		ans = C.com(X - N, N)
		print(ans)

	

if __name__ == '__main__':
	main()