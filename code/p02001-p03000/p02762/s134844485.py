#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n + 1)]
		self.rank = [0] * (n + 1)
		self.size = [1] * (n + 1)

	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]

	def same_check(self, x, y):
		return self.find(x) == self.find(y)

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if self.rank[x] < self.rank[y]:
			if self.same_check(x, y) != True:
				self.size[y] += self.size[x]
				self.size[x] = 0
			self.par[x] = y
		else:
			if self.same_check(x, y) != True:
				self.size[x] += self.size[y]
				self.size[y] = 0
			self.par[y] = x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1

	def siz(self, x):
		x = self.find(x)
		return self.size[x]

#処理内容
def main():
	N, M, K = getlist()

	Dnode = defaultdict(int)
	UF = UnionFind(N)
	for i in range(M):
		A, B = getlist()
		A -= 1; B -= 1
		Dnode[A] += 1
		Dnode[B] += 1
		UF.union(A, B)

	for i in range(N):
		UF.par[i] = UF.find(i)

	Dblock = defaultdict(int)
	for i in range(K):
		C, D = getlist()
		C -= 1; D -= 1
		if UF.same_check(C, D):
			Dblock[C] += 1
			Dblock[D] += 1

	ans = [0] * N
	for i in range(N):
		ans[i] = UF.siz(i) - 1 - Dblock[i] - Dnode[i]

	print(" ".join(list(map(str, ans))))


if __name__ == '__main__':
	main()