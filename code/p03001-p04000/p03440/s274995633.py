class Unionfindtree:
    def __init__(self,number):
        self.par = [i for i in range(number)]
        self.rank = [0]*(number)

    def find(self,x):#親を探す
        if self.par[x] ==x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self,x,y):#x,yを繋げる
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 
        if self.rank[px]<self.rank[py]:
            self.par[px]=py
        else:
            self.par[py]=px
        if self.rank[px]==self.rank[py]:
            self.rank[px] +=1
    
    def connect(self,x,y):#親が同じかみる
        return self.find(x)==self.find(y)
from collections import defaultdict
from heapq import heapify,heappop
import sys
N,M = map(int,input().split())
tree = Unionfindtree(N)
A = [int(i) for i in input().split()]
table=[]
for i in range(M):
    x,y=map(int,input().split())
    tree.union(x,y)

dd=defaultdict(list)
for i in range(N):
    dd[tree.find(i)].append(A[i])
ans=0
g=0
for s in dd.keys():
    heapify(dd[s])
    ans+=heappop(dd[s])
    g+=1
if g==1:
    print(0)
    sys.exit()
if g==2:
    print(ans)
    sys.exit()
L=[]
for s in dd.values():
    L+=list(s)
L.sort()
if len(L)<g-2:
    print('Impossible')
    sys.exit()

ans+=sum(L[:g-2])
print(ans)