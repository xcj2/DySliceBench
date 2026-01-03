# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:26:39 2019
D - 連結 / Connectivity
実行時間制限: 2 sec / メモリ制限: 256 MB
 
配点 : 
400 点
@author: justwah
"""
from collections import Counter
import sys

input = sys.stdin.readline
 
class UnionFind:
    def __init__(self, N):
        self.rank = [0]*N
        self.parent = [i for i in range(N)]
        self.n = N
        
    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
        
    def merge(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] +=1
                
    def same(self, a, b):
        return self.root(a) == self.roob(b)
 
 
n, k, l = map(int, input().split())
 
uf_road = UnionFind(n)
for _ in range(k):
    p, q = map(int, input().split())
    uf_road.merge(p-1, q-1)

uf_rail = UnionFind(n)
for _ in range(l):
    r, s = map(int, input().split())
    uf_rail.merge(r-1, s-1)
    
ctr = Counter()
for i in range(n):  # make a list to count number of cities that both road and rail-wise are in the same group
    r1 = uf_road.root(i)
    r2 = uf_rail.root(i)
    ctr[(r1,r2)] += 1

ans = []
for i in range(n): # print the group size of that city when looped
    r1 = uf_road.root(i)
    r2 = uf_rail.root(i)
    ans.append(ctr[(r1,r2)])

print(*ans)   # * is for unpack the list