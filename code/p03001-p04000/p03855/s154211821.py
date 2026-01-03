# 2019/07/14

from collections import Counter


class unionfind():
    def __init__(self,n):
        self.par=list(range(n+1))
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

uf1=unionfind(n)
uf2=unionfind(n)

for i in range(k):
    p,q=map(int,input().split())
    uf1.unite(p,q)

for i in range(l):
    r,s=map(int,input().split())
    uf2.unite(r,s)

res=[]

for i in range(n+1):
    tmp=(uf1.find(i),uf2.find(i))
    res.append(tmp)
c=Counter(res)
ans=[]
for i in range(n+1):
    ans.append(c[res[i]])
print(*ans[1:])
