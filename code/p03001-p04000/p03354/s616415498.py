class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0]*N
        self.count = 0
    def root(self, a):
        if self.parent[a]==a:
            return a
        else:
            self.parent[a]=self.root(self.parent[a])
            return self.parent[a]
    def size(x):
        return -par[root(x)]

    def is_same(self, a, b):
        return self.root(a)==self.root(b)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1
if __name__ == '__main__':
    n, m=map(int, input().split())
    p=[int(i)-1 for i in input().split()]
    uf = UnionFind(n)
    for i in range(m):
        a,b=map(int, input().split())
        uf.unite(a-1,b-1)
    ans = 0
    for i in range(n):
        if uf.is_same(p[i], i):
            ans+=1
    print(ans)
