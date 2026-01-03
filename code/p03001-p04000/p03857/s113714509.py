from collections import Counter
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[1]*n
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.size[x]>=self.size[y]:
            self.par[y]=x
            self.size[x]+=self.size[y]
        else:
            self.par[x]=y
            self.size[y]+=self.size[x]
n,k,l=map(int,input().split())
uf1=UnionFind(n)
uf2=UnionFind(n)
for _ in range(k):
    u,v=map(int,input().split())
    uf1.unite(u-1,v-1)
for _ in range(l):
    u,v=map(int,input().split())
    uf2.unite(u-1,v-1)
cc=Counter()
for i in range(n):
    cc[(uf1.find(i),uf2.find(i))]+=1
ans=[cc[(uf1.find(i),uf2.find(i))] for i in range(n)]
print(*ans)
    
