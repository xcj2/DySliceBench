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

h,m=map(int, input().split())
s=[list(input()) for i in range(h)]
uf1=UnionFind(h*m)
for i in range(h):
    for j in range(m):
        if s[i][j]!=s[min(i+1,h-1)][j]:uf1.union(i*m+j,i*m+j+m)
        if s[i][j]!=s[i][min(j+1,m-1)]:uf1.union(i*m+j,i*m+j+1)
from collections import Counter
c1=Counter()
c2=Counter()
for i in range(h):
    for j in range(m):
        k = i*m+j
        if s[i][j] == '.':c1[uf1.find(k)] += 1
        else:c2[uf1.find(k)] += 1
ans=0
for i in range(h*m):
    ans+=c1[i]*c2[i]
print(ans)