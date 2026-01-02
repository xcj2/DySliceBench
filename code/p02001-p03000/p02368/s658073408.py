
def scc_decomposition(G):
    n = len(G)
    G_rev = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G_rev[v].append(u)

    # dfs
    vs = []
    visited = [False] * n
    used = [False] * n
    for u in range(n):
        if visited[u]:
            continue
        stack = [u]
        while stack:
            v = stack.pop()
            if used[v]:
                continue
            if not visited[v]:
                visited[v] = True
            else:
                vs.append(v)
                used[v] = True
                continue
            stack.append(v)
            for c in G[v]:
                if not visited[c]:
                    stack.append(c)

    # reverse dfs
    visited = [False] * n
    component = [-1] * n
    for i, u in enumerate(vs[::-1]):
        if visited[u]:
            continue
        stack = [u]
        while stack:
            v = stack.pop()
            visited[v] = True
            component[v] = i
            for c in G_rev[v]:
                if not visited[c]:
                    stack.append(c)

    return component

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        r = x
        while self.parent[r] != r:
            r = self.parent[r]
        while self.parent[x] != r:
            x, self.parent[x] = self.parent[x], r
        return r

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

V, E = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    s, t = map(int, input().split())
    G[s].append(t)
component = scc_decomposition(G)
uf = UnionFind(2 * V)
for v in range(V):
    uf.unite(v, V + component[v])
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    if uf.same(u, v):
        print(1)
    else:
        print(0)
