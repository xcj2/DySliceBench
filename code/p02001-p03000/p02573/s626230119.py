import sys
from collections import deque
mapin = lambda: map(int, sys.stdin.readline().split())
listin = lambda: list(map(int, sys.stdin.readline().split()))
inp = lambda: sys.stdin.readline()

class UnionFind():
    def __init__(self,n):
        self.N = n
        self.par = [-1] * n
    
    def find(self,n):
        if self.par[n] < 0:
            return n
        else:
            self.par[n] = self.find(self.par[n])
            return self.par[n]
    
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        else:
            if -self.par[x] < -self.par[y]:
                x,y = y,x
            self.par[x] += self.par[y]
            self.par[y] = x
    
    def size(self,x):
        return -self.par[self.find(x)]
    
    def tree_num(self):
        res = 0
        for i in self.par:
            res += i < 0
        return res
    
    def same(self,x,y):
        return self.find(x) == self.find(y)
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N,M = mapin()
UF = UnionFind(N)
for i in range(M):
    a,b = mapin()
    a,b = a - 1,b - 1
    UF.unite(a,b)
ans = 0
for i in UF.par:
    if i < 0:
        if ans < -i:
            ans = -i
print(ans)
