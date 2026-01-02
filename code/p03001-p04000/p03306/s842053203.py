from collections import deque


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self, x):
        return -self.root[self.find_root(x)]


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
others = []
UF = UnionFind(n)
for _ in range(m):
    u, v, s = map(int, input().split())
    if not UF.isSameGroup(u, v):
        adj[u].append([v, s])
        adj[v].append([u, s])
        UF.unite(u, v)
    else:
        others.append([u, v, s])

que = deque()
que.append(1)
seen = [0] * (n+1)
seen[1] = 1
val = [0] * (n+1)
plus_min = float('inf')
minus_min = float('inf')
while que:
    v = que.pop()
    for us in adj[v]:
        u, s = us
        if seen[u] == 0:
            que.append(u)
            seen[u] = -seen[v]
            val[u] = s - val[v]
            if seen[u] == -1:
                minus_min = min(minus_min, val[u])
                if minus_min <= 1:
                    print(0)
                    exit()
            else:
                plus_min = min(plus_min, val[u])

x = []
for u, v, s in others:
    if seen[u] != seen[v]:
        if val[u] + val[v] != s:
            print(0)
            exit()
    else:
        if (s - val[u] - val[v]) % 2 == 1:
            print(0)
            exit()
        x_cand = ((s - val[u] - val[v]) // 2) * seen[u]
        if x_cand <= 0:
            print(0)
            exit()
        if plus_min + x_cand <= 0 or minus_min - x_cand <= 0:
            print(0)
            exit()
        if x:
            if x_cand != x[0]:
                print(0)
                exit()
        else:
            x.append(x_cand)

if x:
    print(1)
else:
    if plus_min >= 0:
        print(max(0, minus_min - 1))
    else:
        print(max(0, minus_min - 1 - (-plus_min + 1) + 1))
