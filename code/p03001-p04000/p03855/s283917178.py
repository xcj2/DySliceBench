from collections import defaultdict
class Unionfind:
    def __init__(self,n):
        self.n=n
        self.roots=[i for i in range(self.n)]


    def root(self,x):
        if self.roots[x]==x:
            return x
        else:
            self.roots[x]=self.root(self.roots[x])
            return self.roots[x]
    def unite(self,x,y):
        if self.root(x)==self.root(y):
            return
        else:
            if self.root(x)>self.root(y):
                self.roots[self.root(x)]=self.root(y)
            else:
                self.roots[self.root(y)]=self.root(x)
    
    def same(self,x,y):
        return self.root(x)==self.root(y)

N,K,L=list(input().split(" "))
N=int(N)
K=int(K)
L=int(L)
road=Unionfind(N)
train=Unionfind(N)
for i in range(K):
    p,q=map(int,list(input().split(" ")))
    road.unite(p-1,q-1)
for i in range(L):
    r,s=map(int,list(input().split(" ")))
    train.unite(r-1,s-1)



count=defaultdict(lambda:0)
point=[]
for i in range(N):
    a=road.root(i)
    b=train.root(i)
    l=[a,b]
    point.append(l)
    count[str(l)]+=1
for i in point:
    print(count[str(i)],end=" ")