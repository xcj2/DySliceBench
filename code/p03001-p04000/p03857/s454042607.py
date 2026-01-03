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

# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,k,l = map(int,readline().split())

UF1 = UnionFind(n)
UF2 = UnionFind(n)

for _ in range(k):
    p,q = map(int,readline().split())
    UF1.merge(p-1,q-1)

for _ in range(l):
    r,s = map(int,readline().split())
    UF2.merge(r-1,s-1)

from collections import Counter
d = Counter()
for i in range(n):
    p1 = UF1.root(i)
    p2 = UF2.root(i)
    d[(p1,p2)] += 1

ans = [0]*n
for i in range(n):
    p1 = UF1.root(i)
    p2 = UF2.root(i)
    ans[i] = d[(p1,p2)]

print(*ans)