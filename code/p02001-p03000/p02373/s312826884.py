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

sys.setrecursionlimit(10 ** 7)

class LCA:
    def __init__(self, G, root=0):
        V = len(G)
        K = 1
        while 1 << K < V:
            K += 1
        self.parent = [[-1] * V for _ in range(K)]
        self.dist = [-1] * V
        self.dfs(G, root, -1, 0)
        for k in range(K - 1):
            for v in range(V):
                if self.parent[k][v] < 0:
                    self.parent[k + 1][v] = -1
                else:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]
    
    def dfs(self, G, v, p, d):
        self.parent[0][v] = p
        self.dist[v] = d
        for nv in G[v]:
            if nv != p:
                self.dfs(G, nv, v, d + 1)
    
    def query(self, u, v):
        if self.dist[u] < self.dist[v]:
            u, v = v, u
        K = len(self.parent)
        for k in range(K):
            if (self.dist[u] - self.dist[v]) >> k & 1:
                u = self.parent[k][u]
        
        if u == v:
            return u
        for k in range(K - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        return self.parent[0][u]
    
    def get_dist(self, u, v):
        return self.dist[u] + self.dist[v] - 2 * self.dist[self.query(u, v)]
    
    def on_path(self, u, v, a):
        return self.get_dist(u, a) + self.get_dist(a, v) == self.get_dist(u, v)

n = ni()
kc = nan(n)
q = ni()
uv = nan(q)

g = [[] for _ in range(n)]
for i in range(n):
    k = kc[i][0]
    c = kc[i][1:]
    for j in range(k):
        g[i].append(c[j])

lca = LCA(g)
for i in range(q):
    u, v = uv[i]
    print(lca.query(u, v))
