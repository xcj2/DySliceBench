import sys
input = sys.stdin.readline
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

n,k,l=map(int,input().split())
uf1=UnionFind(n)
for _ in range(k):
    p,q=map(int,input().split())
    uf1.union(p-1,q-1)
uf2=UnionFind(n)
for _ in range(l):
    p,q=map(int,input().split())
    uf2.union(p-1,q-1)
from collections import defaultdict
p=defaultdict(int)
for i in range(n):
    a=uf1.find(i)
    b=uf2.find(i)
    p[(a,b)]+=1
ans=[]
for i in range(n):
    ans.append(p[uf1.find(i),uf2.find(i)])
print(*ans)
