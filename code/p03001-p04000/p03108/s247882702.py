import sys
readline = sys.stdin.readline

N, M = map(int, input().split())
ab = [tuple(map(int, readline().split())) for _ in range(M)]

class UnionFind:
    def __init__(self, size):
        self.rank = [-1]*(size+1)
        self.number = [1]*(size+1)
        
    def find(self, x):
        while self.rank[x] >= 0:
            x = self.rank[x]
        return x
    
    def union(self, a, b):
        if a == b:
            return
        if self.rank[a] == self.rank[b]:
            self.rank[b] = a
            self.rank[a] -= 1
            self.number[a] += self.number[b]
        elif self.rank[a] < self.rank[b]:
            self.rank[b] = a
            self.number[a] += self.number[b]
        else:
            self.rank[a] = b
            self.number[b] += self.number[a]
            
p = N * (N - 1) // 2
ans = [p]
uf = UnionFind(N)

for a, b in ab[1:][::-1]:
    ar = uf.find(a)
    br = uf.find(b)
    
    if ar != br:
        p -= uf.number[ar] * uf.number[br]
        uf.union(ar, br)
    ans.append(p)

print(*ans[::-1], sep='\n')