class UnionFind:
    def __init__(self, n):
        self.sz = [ -1 for i in range(n)]

    # 検索
    def find(self, x):
        if self.sz[x] < 0:
            return x
        else:
            self.sz[x] = self.find(self.sz[x])
            return self.sz[x]


    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.sz[x] > self.sz[y]:
            x,y = y,x
        self.sz[x] += self.sz[y]
        self.sz[y] = x

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def size(self,x):
        return -self.sz[self.find(x)]


N,K,L = map(int,input().split())
ufpq = UnionFind(N)
ufrs = UnionFind(N)
for i in range(K):
    a,b = map(int,input().split())
    ufpq.union(a-1,b-1)
for i in range(L):
    a,b = map(int,input().split())
    ufrs.union(a-1,b-1)

pq = []
rs = []
from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    d[(ufpq.find(i),ufrs.find(i))] += 1

ans = []
for i in range(N):
    ans.append(d[(ufpq.find(i),ufrs.find(i))])
print(" ".join(map(str,ans)))
