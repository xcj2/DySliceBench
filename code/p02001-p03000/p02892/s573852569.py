import sys
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self._size = [1 for _ in range(n)]
        self._edges = 0

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self._size[y] += self._size[x]
            self._edges += 1
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self._size[x] += self._size[y]
            self._edges += 1
    
    def size(self, x):
        x = self.find(x)
        return self._size[x]
    
    def trees(self):
        return self.n - self._edges

    def same(self, x, y):
        return self.find(x) == self.find(y)

n = ni()
s = nsn(n)

def floyd_warshall(n, dist):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

def ok(n, dist):
    uf = UnionFind(2 * n)
    for i in range(n):
        for j in range(n):
            if s[i][j] == '1':
                uf.unite(i, j + n)
                uf.unite(i + n, j)
    for i in range(n):
        if uf.same(i, i + n):
            return False
    return True

dist = [[inf] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == '1':
            dist[i][j] = 1
    dist[i][i] = 0

floyd_warshall(n, dist)

if ok(n, dist):
    ans = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != inf:
                ans = max(dist[i][j], ans)
    print(ans + 1)
else:
    print(-1)