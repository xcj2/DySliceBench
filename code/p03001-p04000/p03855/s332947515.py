n,k,l=map(int,input().split())
road=[list(map(int,input().split())) for _ in range(k)]
rail=[list(map(int,input().split())) for _ in range(l)]

class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
    def same_check(self,x,y):
        return self.find(x)==self.find(y)

from collections import Counter
uf_road=UnionFind(n)
uf_rail=UnionFind(n)
ans=0
for i,j in road:
    uf_road.union(i-1,j-1)
for i,j in rail:
    uf_rail.union(i-1,j-1)
pairs=[None]*n
for i in range(n):
    pairs[i]=(uf_road.find(i), uf_rail.find(i))
cnt=Counter(pairs)
ans=[]
for i in range(n):
    ans.append(cnt[pairs[i]])
print(' '.join(map(str,ans)))