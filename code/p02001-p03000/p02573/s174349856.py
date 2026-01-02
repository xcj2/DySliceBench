import sys; input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

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
		x = self.find(x); y = self.find(y)
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
	N, M = getlist()
	UF = UnionFind(N)
	for i in range(M):
		A, B = getlist()
		A -= 1; B -= 1
		UF.union(A, B)

	#最後に根更新
	for i in range(N):
		UF.par[i] = UF.find(i)

	ans = 0
	# print(UF.size)
	for i in range(N):
		val = UF.size[i]
		ans = max(ans, val)

	print(ans)


if __name__ == '__main__':
	main()