class Tree():
    def __init__(self, n, edge):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - 1].append(e[1] - 1)
            self.tree[e[1] - 1].append(e[0] - 1)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)

    def rerooting(self, func, merge, ti, ei):
        dp = [ti for _ in range(self.n)]
        lt = [ei for _ in range(self.n)]
        rt = [ei for _ in range(self.n)]
        inv = [ei for _ in range(self.n)]
        self.setroot(0)
        for node in self.order[::-1]:
            tmp = ti
            for adj in self.tree[node]:
                if self.parent[adj] == node:
                    lt[adj] = tmp
                    tmp = func(tmp, dp[adj])
            tmp = ti
            for adj in self.tree[node][::-1]:
                if self.parent[adj] == node:
                    rt[adj] = tmp
                    tmp = func(tmp, dp[adj])
            dp[node] = tmp
        for node in self.order:
            if node == 0:
                continue
            merged = merge(lt[node], rt[node])
            par = self.parent[node]
            inv[node] = func(merged, inv[par])
            dp[node] = func(dp[node], inv[node])
        return dp

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

T = Tree(N, E)

def func(node, adj):
    return node * (adj + 1) % M

def merge(lt, rt):
    return lt * rt % M

ti = 1
ei = 0

D = T.rerooting(func, merge, ti, ei)

print('\n'.join(map(str, D)))