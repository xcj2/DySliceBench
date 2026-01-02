class WeighttedUnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n+1)]
		self.rank = [0] * (n+1)
		#根への距離を管理
		self.weight = [0] * (n+1)

	#検索
	def find(self, x):
		if self.par[x] ==x:
			return x
		else:
			y = self.find(self.par[x])
			#根への重みを追加しながら根まで走査
			self.weight[x] +=self.weight[self.par[x]]
			self.par[x] = y
			return y

	def union(self, x, y, w):
		rx = self.find(x)
		ry = self.find(y)

		#xの木の高さ < yの木の高さ
		if self.rank[rx] < self.rank[ry]:
			self.par[rx] = ry
			self.weight[rx] = w - self.weight[x] + self.weight[y]

		#xの木の高さ>=yの木の高さ
		else:
			self.par[ry] = rx
			self.weight[ry] = -w - self.weight[y] + self.weight[x]
			#木の高さが同じだった場合の処理
			if self.rank[rx] == self.rank[ry]:
				self.rank[rx] +=1
	#同じ集合に属するか
	def same(self, x, y):
		return self.find(x) == self.find(y)
	#xからyへのコスト
	def diff(self, x, y):
		return self.weight[x] - self.weight[y]

N, M = map(int, input().split())
wuf = WeighttedUnionFind(N)

for _ in range(M):
	l, r, d = map(int, input().split())

	if not wuf.same(l, r):
		wuf.union(l, r, d)

	else:
		if wuf.diff(l, r) !=d:
			print("No")
			exit()
print("Yes") 
