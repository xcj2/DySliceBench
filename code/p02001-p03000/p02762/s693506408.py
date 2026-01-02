import sys
sys.setrecursionlimit(10 ** 7)


class Tree:
    WHITE = -2
    GRAY = -1
    BLACK = 1

    def __init__(self, adj):
        n = len(adj)
        self.adj = adj
        self.colors = [self.WHITE] * n
        self.depths = [-1] * n
        self.depth = 0

    def init(self):
        self.__init__(self.adj)

    def dfs(self, u, c):
        if self.colors[u] >= 0:
            return

        self.colors[u] = self.GRAY
        self.depths[u] = self.depth

        for v in self.adj[u]:
            if self.colors[v] == self.WHITE:
                self.dfs(v, c)

        self.colors[u] = c

from collections import Counter

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

adj = [[] for _ in range(n)]
for a, b in ab:
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

tree = Tree(adj)
for i in range(n):
    tree.dfs(i, i)

labels = tree.colors

counter = Counter(labels)

ans = [counter[labels[i]] - 1 for i in range(n)]

for a, b in ab:
    a -= 1
    b -= 1
    if labels[a] == labels[b]:
        ans[a] -= 1
        ans[b] -= 1

for c, d in cd:
    c -= 1
    d -= 1
    if labels[c] == labels[d]:
        ans[c] -= 1
        ans[d] -= 1

print(*ans)
