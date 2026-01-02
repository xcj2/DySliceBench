import sys
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs= sys.stdin.buffer.readlines
#rstrip().decode('utf-8')

#import math
#import numpy as np
#import operator
#import bisect
#from heapq import heapify,heappop,heappush
#from math import gcd
#from fractions import gcd
#from collections import deque
#from collections import defaultdict
#from collections import Counter
#from itertools import accumulate
#from itertools import groupby
#from itertools import permutations
#from itertools import combinations
#from scipy.sparse import csr_matrix
#from scipy.sparse.csgraph import floyd_warshall
#from scipy.sparse.csgraph import csgraph_from_dense
#from scipy.sparse.csgraph import dijkstra
#sys.setrecursionlimit(10**7)

#map(int,input().split())



class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
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

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


def main():
	n,m=map(int,input().split())
	uf=WeightedUnionFind(n)
	
	for i in range(m):
		l,r,d=map(int,input().split())
		if uf.same(l,r):
			if d!=uf.diff(l,r):
				print("No")
				exit(0)
		else:
			uf.union(l,r,d)
	print("Yes")
	
if __name__ == '__main__':
	main()