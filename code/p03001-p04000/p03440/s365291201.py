N,M=map(int,input().split())
A=list(map(int,input().split()))
XY=[list(map(int,input().split())) for i in range(M)]
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
for x,y in XY:
    u.unite(x,y)
if u.size(0)==N:
    print(0);exit()
d={}
x=[]
for i,a in enumerate(A):
    r=u.root(i)
    if r not in d:
        d[r]=a
    elif a<d[r]:
        x.append(d[r])
        d[r]=a
    else:
        x.append(a)
rem=2*(N-1-M)-len(d)
print(sum([v for v in d.values()])+sum(sorted(x)[:rem]) if len(x)>=rem else "Impossible")