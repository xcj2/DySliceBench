# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import math
import itertools
import random
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    H,W = inputMap()
    a = []
    for i in range(H):
        tmp = input()
        tmp = "#" + tmp + "#"
        a.append(tmp)
        
    tmp = ""
    for i in range(W+2):
        tmp += "#"
    
    print(tmp)
    for i in a:
        print(i)
    print(tmp)
    
    
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
			# メンバ数の更新
			sum = self.size[x] + self.size[y]
			self.size[x] = sum
			self.size[y] = sum
			# 短いリストを長いリストのルートに繋ぎ直す
			if self.rank[x] < self.rank[y]:
				x, y = y, x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1
			self.par[y] = x
	
	# x と y が同じグループがどうか
	def is_same(self, x, y):
		return self.find(x) == self.find(y)
		
	# x が属するグループのメンバ数を返却
	def getSize(self, x):
		par_x = self.find(x)
		return self.size[par_x]
	
if __name__ == "__main__":
	main()
