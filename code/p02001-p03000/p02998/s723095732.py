import sys
input=sys.stdin.readline
from collections import defaultdict
class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[0]*n
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

n=int(input())
uf=UnionFind(n)
XY=[tuple(map(int,input().split())) for _ in range(n)]
Xd=defaultdict(list)
Yd=defaultdict(list)
for i,(x,y) in enumerate(XY):
    Xd[x].append(i)
    Yd[y].append(i)
for x in Xd:
    i=Xd[x][0]
    for j in Xd[x]:
        uf.union(i,j)
for y in Yd:
    i=Yd[y][0]
    for j in Yd[y]:
        uf.union(i,j)
d=defaultdict(list)
for i in range(n):
    d[uf.find(i)].append(i)
ans=0
for k in d:
    Xs,Ys=set(),set()
    for i in d[k]:
        x,y=XY[i]
        Xs.add(x); Ys.add(y)
    ans+=len(Xs)*len(Ys)
ans-=n
print(ans)