# -*- coding: utf-8 -*-
import sys

def main():
	N, M = map(int, input().split(" "))
	
	WU = WeightedUnionFind(N)
	ans = "Yes"
	for tmp in range(M):
		L, R, D = map(int, input().split(" "))
		L -= 1
		R -= 1
		if WU.is_same(L, R):
			if WU.diff(L, R) != D:
				ans = "No"
		else:
			WU.union(L, R, D)
	
	print(ans)
		
class WeightedUnionFind(object):
	def __init__(self, n=1):
		self.par = [i for i in range(n)]
		self.rank = [0 for _ in range(n)]
		# 親への重みを管理
		self.weight = [0 for _ in range(n)]
		
	# x が属するグループを探索
	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			y = self.find(self.par[x])
			# 親への重みを追加
			self.weight[x] += self.weight[self.par[x]]
			self.par[x] = y
			return self.par[x]
		
	# x と y のグループを結合
	def union(self, x, y, w):
		rx = self.find(x)
		ry = self.find(y)
		# xの木の高さ < yの木の高さ
		if self.rank[rx] < self.rank[ry]:
			self.par[rx] = ry
			self.weight[rx] = w - self.weight[x] + self.weight[y]
		# xの木の高さ ≧ yの木の高さ
		else:
			self.par[ry] = rx
			self.weight[ry] = -w - self.weight[y] + self.weight[x]
			# 木の高さが同じだった場合の処理
			if self.rank[rx] == self.rank[ry]:
				self.rank[rx] += 1
	
	# x と y が同じグループがどうか
	def is_same(self, x, y):
		return self.find(x) == self.find(y)
		
	# x から yへの重みは？
	def diff(self, x, y):
		return self.weight[x] - self.weight[y]
	
if __name__ == "__main__":
	main()
	