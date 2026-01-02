import sys
sys.setrecursionlimit(1000000)



# グラフ定義
class Edge:
    def __init__(self, f: int, t: int, cost: int):
        self._t = t
        self._cost = cost
        self._f = f

    @property
    def t(self):
        return self._t

    @property
    def f(self):
        return self._f

    @property
    def cost(self):
        return self._cost


INF = 1 << 28


# ここから本実装
def bellman_ford(n: int, edges, s: int):
    dist = [INF for _ in range(n)]
    dist[s] = 0

    for i in range(2 * n):
        for e in edges:

            if dist[e.t] > dist[e.f] + e.cost:
                dist[e.t] = dist[e.f] + e.cost
                if i >= n - 1:
                    return None

    return dist


def visitable_node(n, g, rg):

    vis = [False] * n

    def dfs(idx):
        vis[idx] = True
        for e in g[idx]:
            if not vis[e]:
                dfs(e)

    dfs(0)

    rvis = [False] * n

    def rdfs(idx):
        rvis[idx] = True
        for e in rg[idx]:
            if not rvis[e]:
                rdfs(e)

    rdfs(n - 1)

    return [vis[i] & rvis[i] for i in range(n)]


n, m, p = map(int, input().split())

edges = []
g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append(Edge(a, b, -c + p))
    g[a].append(b)
    rg[b].append(a)

visitable = visitable_node(n, g, rg)
updated = [e for e in edges if visitable[e.f] and visitable[e.t]]

dist = bellman_ford(n, updated, 0)

if dist:
    print(max(0, -dist[n - 1]))
else:
    print(-1)
