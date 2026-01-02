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
		self.par = [i for i in range(n)]
		self.rank = [0] * n
		self.size = [1] * n

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
	N = int(input())
	Lx = []
	Ly = []
	UF = UnionFind(N)
	for i in range(N):
		x, y = getlist()
		Lx.append([x, y, i])
		Ly.append([y, x, i])
	Lx = sorted(Lx)
	Ly = sorted(Ly)
	for i in range(N - 1):
		if Lx[i][0] == Lx[i + 1][0]:
			UF.union(Lx[i][2] , Lx[i + 1][2])
		if Ly[i][0] == Ly[i + 1][0]:
			UF.union(Ly[i][2] , Ly[i + 1][2])
	for i in range(N):
		UF.par[i] = UF.find(i)

	nodeX = [[] for i in range(N)] 
	nodeY = [[] for i in range(N)]
	PAR = UF.par
	for i in range(N):
		nodeX[PAR[Lx[i][2]]].append(Lx[i][0])
		nodeY[PAR[Lx[i][2]]].append(Lx[i][1])
	# print(nodeX)
	# print(nodeY)

	#計算
	ans = 0
	D = defaultdict(int)
	for i in range(N):
		if D[PAR[i]] == 0:
			D[PAR[i]] = 1
			ans += len(set(nodeX[PAR[i]])) * len(set(nodeY[PAR[i]])) - UF.size[PAR[i]]
	print(ans) 



if __name__ == '__main__':
	main()