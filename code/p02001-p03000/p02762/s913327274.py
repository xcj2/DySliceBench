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
readline = sys.stdin.readline
read = sys.stdin.read

#n,*a = [int(i) for i in read().split()]
#a = [int(i) for i in readline().split()]
#n = int(input())


n,m,k = [int(i) for i in readline().split()]
ab = [[int(i)-1 for i in readline().split()] for _ in range(m)]
cd = [[int(i)-1 for i in readline().split()] for _ in range(k)]

UF = UnionFind(n)
for a,b in ab:
    UF.merge(a,b)


ans = [UF.getsize(i)-1 for i in range(n)]

for a,b in ab:
    ans[a] -= 1
    ans[b] -= 1

for c,d in cd:
    if UF.issame(c,d):
        ans[c] -= 1
        ans[d] -= 1

print(*ans)







