class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[0]*(n)
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def same_check(self,x,y):
        return self.find(x)==self.find(y)
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1

from collections import Counter

n,k,l=map(int,input().split())
uf1=UnionFind(n)
uf2=UnionFind(n)

for i in range(k):
    x,y=map(int,input().split())
    uf1.union(x-1,y-1)

for i in range(l):
    x,y=map(int,input().split())
    uf2.union(x-1,y-1)

#for i in range(n):
#uf1.find(i)
#uf2.find(i)

ctr=Counter()
for i in range(n):
    r1 = uf1.find(i)
    r2 = uf2.find(i)
    ctr[(r1,r2)]+=1

ans=[]
for i in range(n):
    r1 = uf1.find(i)
    r2 = uf2.find(i)
    ans.append(ctr[(r1,r2)])
print(*ans)