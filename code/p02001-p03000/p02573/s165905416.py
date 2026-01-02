def INT():
    return int(input())

def LI():
    return list(map(int, input().split()))

def MI():
    return map(int, input().split())

class UnionFind:
    def __init__(self, N):
        self.root = [_ for _ in range(N)]
        self.rank = [0] * N
        self.size = [1] * N
        
    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            #パス圧縮
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            if self.rank[x] > self.rank[y]:
                self.size[x] += self.size[y]
                self.root[y] = x
            else:
                self.size[y] += self.size[x]
                self.root[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
            
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def getSizeOfSet(self, x):
        return self.size[self.find(x)]

import sys
sys.setrecursionlimit(10**9)

N, M = MI()
friend = UnionFind(N)

for _ in range(M):
    A, B = MI()
    friend.union(A - 1, B - 1)
    
ans = 0
for i in range(N):
    ans = max(ans, friend.getSizeOfSet(i))
    
print(ans)