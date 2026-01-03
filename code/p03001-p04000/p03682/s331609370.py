N=int(input())
x,y=map(list,zip(*[list(map(int,input().split())) for i in range(N)]))
x=sorted(zip(x,range(N)))
y=sorted(zip(y,range(N)))
from heapq import heappop,heappush
qx,qy=[(10**9+1,0,0)],[(10**9+1,0,0)]
for i in range(N-1):
    heappush(qx,(x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    heappush(qy,(y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
r=0
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
while u.size(0)<N:
    d,i,j=heappop(qx) if qx[0]<qy[0] else heappop(qy)
    if u.unite(i,j):
        r+=d
print(r)