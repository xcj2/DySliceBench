N,M = map(int,input().split())
src = [tuple(map(int,input().split())) for i in range(M)]

def comb(n):
    return n*(n+1)//2

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0
        self.size = [1] * N
        self.connection = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        self.connection -= (comb(self.size[ra]) + comb(self.size[rb]))
        self.connection += comb(self.size[ra] + self.size[rb])
        if self.rank[ra] < self.rank[rb]:
            self.size[rb] += self.size[ra]
            self.parent[ra] = rb
        else:
            self.size[ra] += self.size[rb]
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1

uf = UnionFind(N)
ans = [N*(N-1)//2]

for a,b in list(reversed(src))[:-1]:
    a,b = a-1,b-1
    uf.unite(a,b)
    ans.append(ans[0] - uf.connection)

print(*ans[::-1], sep='\n')