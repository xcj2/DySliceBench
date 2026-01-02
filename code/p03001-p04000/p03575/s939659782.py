# -*- coding: utf-8 -*-
import sys

def main():
	p, l = map(int, input().split(" "))
	
	lines = []
	for i in range(l):
		a, b = map(int, input().split(" "))
		a, b = a - 1, b - 1
		lines.append((a, b))
		
	result = 0
	for i, val in enumerate(lines):
		uf = UnionFind(p)
		for i, val2 in enumerate(lines):
			if val == val2:
				continue
			a, b = val2
			uf.union(a, b)
			
		aa, _ = lines[0]
		for i in range(p):
			if uf.is_same(aa, i) == False:
				result = result + 1
				break
				
	print(result)

class UnionFind(object):
	def __init__(self, n=1):
		self.par = [i for i in range(n)]
		self.rank = [0 for _ in range(n)]
		
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
			if self.rank[x] < self.rank[y]:
				x, y = y, x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1
			self.par[y] = x
	
	# x と y が同じグループがどうか
	def is_same(self, x, y):
		return self.find(x) == self.find(y)
		
if __name__ == "__main__":
	main()
	