# coding: utf-8
# Your code here!
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) #親ノード
        self.size = [1]*n #グループの要素数
 
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
        return True
 
    def issame(self, x, y): #same(x,y): xとyが同じ組ならTrue
        return self.root(x) == self.root(y)
        
    def getsize(self,x): #size(x): xのいるグループの要素数を返す
        return self.size[self.root(x)]

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())
xyi = []
for i in range(n):
    x,y = [int(i) for i in readline().split()]
    xyi.append((x,y,i))


Xyi = sorted(xyi)
xYi = sorted(xyi, key=lambda x: x[1])

from heapq import *

a = []

for j in range(n-1):
    x,y,i = Xyi[j]
    xx,yy,ii = Xyi[j+1]
    heappush(a,(xx-x,ii,i))
    x,y,i = xYi[j]
    xx,yy,ii = xYi[j+1]
    heappush(a,(yy-y,ii,i))

#print(a)

uf = UnionFind(n)
c = 1
ans = 0
while c < n:
    d,ii,i = heappop(a)
#    print(d,ii,i)
    if uf.merge(ii,i):
        c += 1
        ans += d
#        print(c,ans,ii,i)

print(ans)    
    
    









