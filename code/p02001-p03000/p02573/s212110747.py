ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil
n,m = ma()
class unionfind():
    def __init__(self,n):
        self.par = list(range(n))
        self.size = [1]*n
        self.rank = [0]*n
        self.n = n
    def root(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self,x,y):
        return self.root(x) == self.root(y)

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:return
        else:
            if self.rank[x] < self.rank[y]:
                 x,y = y,x
            if self.rank[x] == self.rank[y]:
                self.rank[x]+=1
            self.par[y] = x
            self.size[x] +=self.size[y]
    def get_size(self,x):
        x = self.root(x)
        return self.size[x]
    def parent_set(self):
        for x in range(self.n):
            self.root(x)
        s = set()
        for par in self.par:
            s.add(par)
        return s
uf = unionfind(n)
for i in range(m):
    a,b = ma()
    a-=1;b-=1
    uf.unite(a,b)
ans = 0
for i in range(n):
    ans=max(ans,uf.get_size(i))
print(ans)
