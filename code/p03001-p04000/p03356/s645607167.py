# -*- coding: utf-8 -*-
def inpl(): return map(int, input().split())

class UnionFindTree():
    
    def __init__(self, N):
        self.parent = [-1]*(N+1)
        self.rank = [1]*(N+1)
        self.size = [1]*(N+1)
  
    def find(self, i):
        if self.parent[i] == -1:
            group = i
        else:
            group = self.find(self.parent[i]) 
            self.parent[i] = group
        return group
      
    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] == self.rank[py]: # rank is same
                self.rank[px] += 1
            elif self.rank[px] < self.rank[py]:
                px, py = py, px
                
            self.parent[py] = px
            self.size[px] += self.size[py]
    
    def getsize(self, x):
        return self.size[self.find(x)]
    
    def groups(self, index1=True):
        return set([self.find(i) for i in range(0+index1, N+index1)])

N, M = inpl()
P = list(inpl())

UFT = UnionFindTree(N)
for m in range(M):
    x, y = inpl()
    UFT.unite(x, y)

ans = sum([UFT.find(i) == UFT.find(p) for i, p in enumerate(P, start=1)])
print(ans)