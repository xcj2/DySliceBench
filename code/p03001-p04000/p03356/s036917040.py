class UnionFind:
    parent = []
    rank = []

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
                return self.rank[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    uf = UnionFind(N)
    
    for _ in range(M):
        a, b = map(int, input().split())
        uf.unite(a-1, b-1)
    
    ans = 0
    for i in range(N):
        if uf.isSame(i, A[i] -1):
            ans += 1

    return ans

print(solve())