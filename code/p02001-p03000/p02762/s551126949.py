# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
import collections
import copy
import heapq
from collections import defaultdict
from heapq import heappop, heappush
import itertools
input = sys.stdin.readline

##### リストの 二分木検索 #####
# bisect_left(lists, 3)
# bisect_right(lists, 3)

##### プライオリティキュー #####
# heapq.heapify(a) #リストaのheap化
# heapq.heappush(a,x) #heap化されたリストaに要素xを追加
# heapq.heappop(a) #heap化されたリストaから最小値を削除＆その最小値を出力

# heapq.heappush(a, -x) #最大値を取り出す時は、pushする時にマイナスにして入れよう
# heapq.heappop(a) * (-1) #取り出す時は、-1を掛けて取り出すこと

##### タプルリストのソート #####
# sorted(ans) #(a, b) -> 1st : aの昇順, 2nd : bの昇順
# sorted(SP, key=lambda x:(x[0],-x[1])) #(a, b) -> 1st : aの昇順, 2nd : bの降順
# sorted(SP, key=lambda x:(-x[0],x[1])) #(a, b) -> 1st : aの降順, 2nd : bの昇順
# sorted(SP, key=lambda x:(-x[0],-x[1])) #(a, b) -> 1st : aの降順, 2nd : bの降順

# sorted(SP, key=lambda x:(x[1])) #(a, b) -> 1st : bの昇順
# sorted(SP, key=lambda x:(-x[1])) #(a, b) -> 1st : bの降順

##### 累乗 #####
# pow(x, y, z) -> x**y % z

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))

inf = float('inf')
mod = 1000000007

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

def main():
	N,M,K = inputMap()
	UF = UnionFind(N)
	AB = {}
	for i in range(N):
		AB[i] = []
	for i in range(M):
		a,b = inputMap()
		a -= 1
		b -= 1
		UF.union(a, b)
		if a in AB:
			AB[a].append(b)

		if b in AB:
			AB[b].append(a)

	CD = {}
	for i in range(N):
		CD[i] = []
	for i in range(K):
		c,d = inputMap()
		c -= 1
		d -= 1
		if c in CD:
			CD[c].append(d)

		if d in CD:
			CD[d].append(c)

	ans = []
	for i in range(N):
		tmp = UF.getSize(i) - len(AB[i]) -1
		for j in CD[i]:
			if UF.is_same(i, j):
				tmp -= 1
		ans.append(tmp)

	print(*ans)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# special thanks :
#  https://nagiss.hateblo.jp/entry/2019/07/01/185421
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#https://www.kumilog.net/entry/union-find

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

# nCr mod m
# rがn/2に近いと非常に重くなる

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

# mを法とするaの乗法的逆元
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# nHr mod m
# 問題によって、combination()を切り替えること
def H(n, r, mod=10**9+7):
	# comb = Combination(n+r-1, mod)
	# return comb(n+r-1, r)
    return combination(n+r-1, r, mod)

class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

if __name__ == "__main__":
	main()
