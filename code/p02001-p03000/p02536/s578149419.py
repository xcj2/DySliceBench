def readInt():
    return int(input())
def readList():
    return list(map(int,input().split()))
def readMap():
	return map(int,input().split())
def readStr():
    return input()
inf=float('inf')
mod = 10**9+7
import math
from itertools import permutations
class DSU:
    def __init__(self,n):
        self.par=list(range(n))
        self.sz=[1]*(n)
    def find(self,x):
        if x!=self.par[x]:
            self.par[x]=self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x!=y:
            if self.sz[y]>self.sz[x]:
                x,y=y,x
            self.par[y]=x
            self.sz[x]+=self.sz[y]
            self.sz[y]=self.sz[x]
            return True
        return False
    def parent(self,x):
        return self.par[x]

def solve(N,A):
    dsu=DSU(N)
    for a,b in A:
        dsu.union(a-1,b-1)
    cnt=0
    for i in range(N):
        if dsu.parent(i)==i:
            cnt+=1
    return cnt-1



N,M=readMap()
A=[]
for _ in range(M):
    a,b=readMap()
    A.append((a,b))
print(solve(N,A))