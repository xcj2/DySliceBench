import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)
        self.sizes = [1] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w=1):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.sizes[ry] += self.size(rx)
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.sizes[rx] += self.size(ry)
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

    def size(self, x):
        return self.sizes[self.find(x)]

uf=WeightedUnionFind(n)
for a,b in ab:
    uf.union(a,b)

# print(uf.par)
dic={}
for i in range(n):
    pa=uf.find(i+1)
    if pa in dic:
        dic[pa]+=1
    else:
        dic[pa]=1

ans=0
for i in dic.values():
    ans=max(ans,i)
print(ans)