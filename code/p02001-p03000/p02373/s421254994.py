from collections import defaultdict

class Tree:
    def __init__(self, N):
        self.N = N
        self.D = (self.N-1).bit_length()
        self.E = defaultdict(dict)
    
    def add_edge(self, init, end, weight, undirected=False):
        self.E[init][end] = weight
        if undirected: self.E[end][init] = weight
    
    def dfs(self, root):
        # parents[v]: the parent of the vertex v
        # depth[v]: the depth of the vertex v from the root
        # dist[v]: the distance of the vertex v from the root.
        self.parent = [None] * self.N
        self.depth = [-1] * self.N
        self.dist = [float('inf')] * self.N
        self.parent[root] = -1; self.depth[root] = 0; self.dist[root] = 0;
        stack = [root]
        while stack:
            v = stack.pop()
            for u in self.E[v].keys():
                if self.depth[u] != -1: continue
                self.parent[u] = v
                self.depth[u] = self.depth[v] + 1
                self.dist[u] = self.dist[v] + self.E[v][u]
                stack.append(u)
    
    def doubling(self):
        # O(N log N) time
        self.next = [self.parent]
        for d in range(1, self.D):
            self.next.append([self.next[d-1][self.next[d-1][v]] if self.next[d-1][v] != -1 else -1 for v in range(self.N)])
    
    def lca(self, u, v):
        # O(log N) time
        # the depth of v is set to be no less than that of u
        if self.depth[u] > self.depth[v]: u, v = v, u
        # find the ancestor of v with the same depth as that of u
        diff = self.depth[v] - self.depth[u]
        for i in range(diff.bit_length()):
            if diff & 1: v = self.next[i][v]
            diff >>= 1
        if u == v: return u
        for i in range(self.D-1, -1, -1):
            pu, pv = self.next[i][u], self.next[i][v]
            if pu != pv: u, v = pu, pv
        return self.next[0][u]

n = int(input())
tr = Tree(n)
for i in range(n):
    k, *C, = map(int, input().split())
    for c in C:
        tr.add_edge(i, c, 1, undirected=True)
tr.dfs(0)
tr.doubling()
q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(tr.lca(u, v))
