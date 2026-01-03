# -*- coding: utf-8 -*-
from operator import itemgetter

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n)]

    def same(self, x, y):
        return self.root(x)==self.root(y)

    def root(self, x):
        if self.par[x]<0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return

        if self.par[x]>self.par[y]:
            x,y = y,x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self,x):
        return -self.par[self.root(x)]

def kruskal(e,n):
    l = []
    for v in range(n):
        for u,c in e[v]:
            l.append((c,v,u))
    l.sort()

    uf = UnionFind(n)
    cost = 0
    res = []
    for c,v,u in l:
        if uf.same(v,u):
            continue
        res.append((v,u,c))
        cost += c
        uf.unite(v,u)
    return res,cost


n = int(input())
e = [[] for _ in range(n)]

ixy = []
for i in range(n):
    x,y = map(int, input().split())
    ixy.append((i,x,y))

ixy.sort(key=itemgetter(1,2))
for i in range(n-1):
    v,a,b = ixy[i]
    u,c,d = ixy[i+1]
    e[v].append((u,min(abs(a-c),abs(b-d))))

ixy.sort(key=itemgetter(2,1))
for i in range(n-1):
    v,a,b = ixy[i]
    u,c,d = ixy[i+1]
    e[v].append((u,min(abs(a-c),abs(b-d))))

r,cost = kruskal(e,n)
print(cost)