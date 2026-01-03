ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys
input=sys.stdin.readline
class unionfind():
    def __init__(self,n):
        self.par = list(range(n))
        self.size = [1]*n
        self.rank = [0]*n
        self.n = n
        #self.ps=set(range(n)) #not tested
    def root(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self,x,y):
        return self.root(x) == self.root(y)

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:return
        else:
            if self.rank[x] < self.rank[y]:
                 x,y = y,x
            if self.rank[x] == self.rank[y]:
                self.rank[x]+=1
            self.par[y] = x
            #self.ps.discard(y)##親の集合からyを取り除く
            self.size[x] +=self.size[y]
    def get_size(self,x):
        x = self.root(x)
        return self.size[x]
    def parent_set(self):
        for x in range(self.n):
            self.root(x)
        s = set()
        for par in self.par:
            s.add(par)
        return s

"""
edges :: [(cost,u,v) for every Edge]
"""
def Kruskal(edges,n):
    tot=0
    edges.sort()
    uf = unionfind(n)
    for cost,u,v in edges:
        if uf.same(u,v):
            pass
        else:
            uf.unite(u,v)
            tot+=cost
    return tot

xy=[]
n = ni()
for i in range(n):
    x,y=lma()
    xy.append((i,x,y))
xy.sort(key=lambda x:x[1])
#print(xy)
ed=[]
INF=10**15
ip=INF
xp=INF
yp=INF
for i,x,y in xy:
    if ip!=INF:
        ed.append((x-xp,i,ip))
    ip=i;xp=x;yp=y

xy.sort(key=lambda x:x[2])
#print(xy)
ip=INF
xp=INF
yp=INF
for i,x,y in xy:
    if ip!=INF:
        ed.append((y-yp,i,ip))
    ip=i;xp=x;yp=y
#print(ed)
print(Kruskal(ed,n))
