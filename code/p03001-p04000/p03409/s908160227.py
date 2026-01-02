import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

class MaxFlow:
    def __init__(self, node_count):
        self.node_count = node_count
        self.graph = [[] for _ in range(node_count)]

    def add_edge(self, u, v, cap):
        idx1 = len(self.graph[v])
        idx2 = len(self.graph[u])
        self.graph[u].append([v, cap, idx1])
        self.graph[v].append([u,   0, idx2])

    def dfs(self, u, t, f):
        if u == t:
            return f
        self.used[u] = True
        for i in range(len(self.graph[u])):
            v, cap, rev = self.graph[u][i]
            if self.used[v] == False and cap > 0:
                d = self.dfs(v, t, min(f, cap))
                if d:
                    self.graph[u][i][1] -= d
                    self.graph[v][rev][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.used = [False] * self.node_count
            f = self.dfs(s, t, 1 << 29)
            if not f:
                return flow
            flow += f



n = getint()
a = [getints() for _ in range(n)]
b = [getints() for _ in range(n)]

src = n + n
dst = src + 1
nv = dst + 1
mf = MaxFlow(nv)

for i in range(n):
    mf.add_edge(src, i, 1)
    mf.add_edge(i + n, dst, 1)

for i in range(n):
    for j in range(n):
        if a[i][0] < b[j][0] and a[i][1] < b[j][1]:
            mf.add_edge(i, j + n, 1)

print (mf.max_flow(src, dst))