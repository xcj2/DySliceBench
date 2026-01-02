# -*- coding: utf-8 -*-
import sys
import collections

def main():
	N, M = map(int, input().split(" "))
	
	bridge = []
	for _ in range(M):
		a, b = map(int, input().split(" "))
		bridge.append((a, b))
		
	bridge.reverse()
	uf = UnionFind(N)
	ans = []
	fuben = 0
	ans.append(N * (N-1) // 2)
	
	for i, val in enumerate(bridge):
		a, b = val
		a, b = a-1, b-1
		if False == uf.is_same(a, b):
			child_a = uf.getCoun(a)
			child_b = uf.getCoun(b)
			ans.append(ans[i] - (child_a * child_b))
		else:
			ans.append(ans[i])
		uf.union(a, b)
		
	ans.pop()
	ans.reverse()
	for val in ans:
		print(val)
	

class UnionFind(object):
	def __init__(self, n=1):
		self.par = [i for i in range(n)]
		self.rank = [0 for _ in range(n)]
		self.size = [1 for _ in range(n)]
		
	# x が属するグループを探索
	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]
		
	# x と y のグループを結合
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x != y:
			x_size = self.size[x]
			y_size = self.size[y]
			sum = x_size + y_size
			self.size[x] = sum
			self.size[y] = sum
			if self.rank[x] < self.rank[y]:
				x, y = y, x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1
			self.par[y] = x
	
	# x と y が同じグループがどうか
	def is_same(self, x, y):
		return self.find(x) == self.find(y)
		
	def getCoun(self, a):
		x = self.find(a)
		return self.size[x]

if __name__ == "__main__":
	main()
	