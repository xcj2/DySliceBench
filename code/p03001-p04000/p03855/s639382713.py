from collections import defaultdict as dd

class UnionFind(object):
    def __init__(self,n):
        self.parent={i:i for i in range(1,n+1)}
        self.size={i:1 for i in range(1,n+1)}
    def find(self,a):
        if self.parent[a]!=a:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]
    def unite(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:return
        if self.size[a]>self.size[b]:
            self.size[a]+=self.size[b]
            self.parent[b]=a
        else:
            self.size[b]+=self.size[a]
            self.parent[a]=b
    def isunited(self,a,b):
        return self.find(a)==self.find(b)

n,k,l=map(int,input().split())
uft_road=UnionFind(n)
uft_train=UnionFind(n)

for _ in range(k):
    p,q=map(int,input().split())
    uft_road.unite(p,q)

for _ in range(l):
    r,s=map(int,input().split())
    uft_train.unite(r,s)

dc=dd(int)
du={}
for i in range(1,n+1):
    du[i]=(uft_road.find(i),uft_train.find(i))
    dc[du[i]]+=1

print(*(dc[du[i]] for i in range(1,n+1)))