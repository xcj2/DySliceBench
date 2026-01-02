# coding: utf-8
# Your code here!
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) #親ノード
        self.size = [1]*n #グループの要素数
        self.cycle = [0]*n
 
    def root(self, x): #root(x): xの根ノードを返す．
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 
 
    def merge(self, x, y): #merge(x,y): xのいる組とyのいる組をまとめる
        x, y = self.root(x), self.root(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x,y=y,x #xの要素数が大きいように
        self.size[x] += self.size[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        self.cycle[x] = self.cycle[x]+self.cycle[y]
        return True
 
    def issame(self, x, y): #same(x,y): xとyが同じ組ならTrue
        return self.root(x) == self.root(y)
        
    def getsize(self,x): #size(x): xのいるグループの要素数を返す
        return self.size[self.root(x)]

    def getcycle(self,x): #size(x): xのいるグループの要素数を返す
        return self.cycle[self.root(x)]

    def addcycle(self,x): #size(x): xのいるグループの要素数を返す
        self.cycle[self.root(x)]+=1
        return 

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意
 
#n = int(input())
n,h,w = [int(i) for i in readline().split()]
#a = [int(i) for i in readline().split()]

uf = UnionFind(h+w)

rca = [[int(i)-1 for i in readline().split()] for i in range(n)]

from operator import itemgetter
rca.sort(key = itemgetter(2), reverse=True)

ans = 0
#print(rca)
for r,c,a in rca:
    c += h
    a += 1
    if uf.issame(r,c):
        if uf.getcycle(r): continue
        ans += a
        uf.addcycle(r)
    else:
        if uf.getcycle(r)+uf.getcycle(c) >= 2: continue
        uf.merge(r,c)
        ans += a

print(ans)












    