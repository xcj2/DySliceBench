N,M,K=map(int, input().split())

class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

ans=[0]*N
uf1=UnionFind(N)
for i in range(M):  # range(m):
    a,b=map(int, input().split()) #a,b:つながっている辺
    uf1.union(a-1,b-1)
    ans[a-1]-=1
    ans[b-1]-=1

for i in range(N):
    uf1.find(i)  # 一周findすることによって接続漏れをなくす。

from collections import defaultdict
ll=defaultdict(int)
for i in uf1.par:
    ll[i]+=1

for i in range(N):
    ans[i]+=ll[uf1.par[i]]-1

for i in range(K):
    a,b=map(int, input().split()) #a,b:つながっている辺
    if uf1.is_same(a-1,b-1):
        ans[a-1]-=1
        ans[b-1]-=1

print(*ans)