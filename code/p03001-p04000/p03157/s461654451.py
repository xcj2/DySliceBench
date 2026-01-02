import numpy as np
from itertools import product
import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            else:
                self.par[y] = x
            
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
uf = UnionFind(H*W)

for i, j in product(range(H), range(W-1)):
    if S[i][j] != S[i][j+1]:
        uf.unite(i*W+j, i*W+j+1)

for i, j in product(range(H-1), range(W)):
    if S[i][j] != S[i+1][j]:
        uf.unite(i*W+j, (i+1)*W+j)

whitecnt = np.zeros(H*W, dtype=int)
blackcnt = np.zeros(H*W, dtype=int)

for i, j in product(range(H), range(W)):
    if S[i][j] == '.':
        whitecnt[uf.find(i*W+j)] += 1
    else:
        blackcnt[uf.find(i*W+j)] += 1

print(np.sum(whitecnt*blackcnt))