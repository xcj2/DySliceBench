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

class Factorial():
    def __init__(self, n, mod):
        self.mod = mod
        self.factorial = [0 for _ in range(n + 1)]
        self.inv = [0 for _ in range(n + 1)]
        self.factorial[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.factorial[i + 1] = self.factorial[i] * (i + 1) % mod
        self.inv[n] = pow(self.factorial[n], mod - 2, mod)
        for i in range(n)[::-1]:
            self.inv[i] = self.inv[i + 1] * (i + 1) % mod

    def fact(self, m):
        return self.factorial[m]

    def invfact(self, m):
        return self.inv[m]

import sys
input = sys.stdin.readline

MOD = 1000000007

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

T = Tree(N, E)
F = Factorial(N + 1, MOD)

def func(node, adj):
    size = node[1] + adj[1]
    count = node[0] * adj[0] * F.invfact(adj[1]) * F.fact(size - 1) * F.invfact(node[1] - 1)
    count %= MOD
    return count, size

def merge(lt, rt):
    size = lt[1] + rt[1] - 1
    count = lt[0] * rt[0] * F.invfact(lt[1] - 1) * F.invfact(rt[1] - 1) * F.fact(size - 1)
    count %= MOD
    return count, size

ti = (1, 1)
ei = (1, 0)

D = T.rerooting(func, merge, ti, ei)

res = []

for i in range(N):
    res.append(D[i][0])

print('\n'.join(map(str, res)))