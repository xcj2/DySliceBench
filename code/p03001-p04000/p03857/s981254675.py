N,K,L=map(int,input().split())
pq=[list(map(int,input().split())) for i in range(K)]
rs=[list(map(int,input().split())) for i in range(L)]
class UnionFind:
    def __init__(self,N):
        self.Parent=[-1]*N
    def unite(self,m,n):
        rm=self.root(m)
        rn=self.root(n)
        if rm==rn:
            return False
        else:
            if self.size(rm)<self.size(rn):
                rm,rn=rn,rm
            self.Parent[rm]+=self.Parent[rn]
            self.Parent[rn]=rm
            return True
    def root(self,n):
        if self.Parent[n]<0:
            return n
        else:
            self.Parent[n]=self.root(self.Parent[n])
            return self.Parent[n]
    def size(self,n):
        return -self.Parent[self.root(n)]
u=UnionFind(N)
v=UnionFind(N)
for e in pq:
    u.unite(e[0]-1,e[1]-1)
for e in rs:
    v.unite(e[0]-1,e[1]-1)
from collections import defaultdict
d=defaultdict(int)
for i in range(N):
    d[(u.root(i),v.root(i))]+=1
a=[]
for i in range(N):
    a.append(d[(u.root(i),v.root(i))])
print(*a)