ma = lambda : map(int,input().split())
import sys
sys.setrecursionlimit(10**6)
class unionfind():
    def __init__(self,n):
        self.par = list(range(n))
        self.size = [1]*n
        self.rank = [0]*n

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
        if x!=y:
            if self.rank[x] < self.rank[y]:
                 x,y = y,x
            if self.rank[x] < self.rank[y]:
                self.rank[x]+=1
            self.par[y] = x
            self.size[x] +=self.size[y]
    def get_size(self,x):
        x = self.root(x)
        return self.size[x]

n,m = ma()
ans = [0]*m
ab = []
for i in range(m):
    a,b = ma()
    ab.append((a-1,b-1))

uf = unionfind(n)
ans[m-1] = n*(n-1)//2
for i in range(m-1,0,-1):
    a,b = ab[i]
    if uf.same(a,b):
        ans[i-1] = ans[i]
    else:
        ans[i-1] = ans[i] - uf.get_size(a)*uf.get_size(b)
        uf.unite(a,b)
for a in ans:print(a)
