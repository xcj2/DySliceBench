# -*- coding: utf-8 -*-
def inpl(): return list(map(int, input().split()))

class UnionFindTree():
    def __init__(self, N):
        self.parent = [-1]*(N+1)
        self.rank = [1]*(N+1)
        self.size = [1]*(N+1)
        self.huben = N*(N-1)//2
  
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
            self.huben -= self.size[px] * self.size[py]
            self.size[px] += self.size[py]

    def getsize(self, x):
        return self.size[self.find(x)]
    
    def groups(self, index1=True):
        return set([self.find(i) for i in range(0+index1, N+index1)])

N, M = inpl()
A, B = [0]*M, [0]*M

for i in range(M):
    A[i], B[i] = inpl()

ans = []
UFT = UnionFindTree(N)

for i in range(M-1, -1, -1):
    ans.append(UFT.huben)
    UFT.unite(A[i], B[i])

print(*ans[::-1], sep="\n")