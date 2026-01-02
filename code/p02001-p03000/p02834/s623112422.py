class Tree():
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - indexed].append(e[1] - indexed)
            self.tree[e[1] - indexed].append(e[0] - indexed)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        self.size = [1 for _ in range(self.n)]
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)
        for node in self.order[::-1]:
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                self.size[node] += self.size[adj]

    def heavylight_decomposition(self):
        self.order = [None for _ in range(self.n)]
        self.head = [None for _ in range(self.n)]
        self.head[self.root] = self.root
        self.next = [None for _ in range(self.n)]
        stack = [self.root]
        order = 0
        while stack:
            node = stack.pop()
            self.order[node] = order
            order += 1
            maxsize = 0
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                if maxsize < self.size[adj]:
                    maxsize = self.size[adj]
                    self.next[node] = adj
            for adj in self.tree[node]:
                if self.parent[node] == adj or self.next[node] == adj:
                    continue
                self.head[adj] = adj
                stack.append(adj)
            if self.next[node] is not None:
                self.head[self.next[node]] = self.head[node]
                stack.append(self.next[node])

    def range_hld(self, u, v, edge=False):
        res = []
        while True:
            if self.order[u] > self.order[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                res.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.parent[self.head[v]]
            else:
                res.append((self.order[u] + edge, self.order[v] + 1))
                return res

    def subtree_hld(self, u):
        return self.order[u], self.order[u] + self.size[u]

    def lca_hld(self, u, v):
        while True:
            if self.order[u] > self.order[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                v = self.parent[self.head[v]]
            else:
                return u

class SegmentTree():
    def __init__(self, arr, func=min, ie=2**63):
        self.h = (len(arr) - 1).bit_length()
        self.n = 2**self.h
        self.ie = ie
        self.func = func
        self.tree = [ie for _ in range(2 * self.n)]
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(1, self.n)[::-1]:
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def set(self, idx, x):
        idx += self.n
        self.tree[idx] = x
        while idx:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, lt, rt):
        lt += self.n
        rt += self.n
        vl = vr = self.ie
        while rt - lt > 0:
            if lt & 1:
                vl = self.func(vl, self.tree[lt])
                lt += 1
            if rt & 1:
                rt -= 1
                vr = self.func(self.tree[rt], vr)
            lt >>= 1
            rt >>= 1
        return self.func(vl, vr)

import sys
input = sys.stdin.readline

N, u, v = map(int, input().split())
u -= 1; v -= 1
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

t = Tree(N, E)
t.setroot(v)
t.heavylight_decomposition()

d = t.depth[u]
k = (d + 1) // 2 - 1

for _ in range(k):
    u = t.parent[u]

arr = [None for _ in range(N)]
for i in range(N):
    arr[t.order[i]] = t.depth[i]

st = SegmentTree(arr, max, -1)
lt, rt = t.subtree_hld(u)
maxdep = st.query(lt, rt)

print(maxdep - 1)