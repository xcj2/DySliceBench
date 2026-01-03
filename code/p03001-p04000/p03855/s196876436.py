# 2019/07/13
# Union-Find
# Disjoint-Set

import sys
from collections import Counter
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

class union_find():
    def __init__(self,n):
        self.par=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def is_same(self,x,y):
        return self.find(x)==self.find(y)
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1


n,k,l=map(int,input().split())
res=[1]*(n+1)
uf1=union_find(n)
for i in range(k):
    p,q=map(int,input().split())
    uf1.unite(p,q)

uf2=union_find(n)
for i in range(l):
    r,s=map(int,input().split())
    uf2.unite(r,s)

res=[]
for i in range(n+1):
    res.append((uf1.find(i),uf2.find(i)))
c=Counter(res)

ans=[]

for i in range(n+1):
    ans.append(c[res[i]])
print(*ans[1:])