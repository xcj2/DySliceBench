from collections import deque

INFTY = 1 << 30

class Edge:
    def __init__(self, t, w):
        self.t = t
        self.w = w


def bfs(s, n, g):
    d = [INFTY] * n
    q = deque()
    q.append(s)
    d[s] = 0
    while len(q) != 0:
        u = q.popleft()
        for i in range(len(g[u])):
            e = g[u][i]
            if d[e.t] == INFTY:
                d[e.t] = d[u] + e.w
                q.append(e.t)
    return d


def solve(n, g):
    d = bfs(0, n, g)
    maxv = 0
    tgt = 0
    for i in range(n):
        if d[i] == INFTY:
            continue
        if maxv < d[i]:
            maxv = d[i]
            tgt = i

    d = bfs(tgt, n, g)
    maxv = 0
    for i in range(n):
        if d[i] == INFTY:
            continue
        maxv = max(maxv, d[i])

    print(maxv)




if __name__ == '__main__':
    n = int(input())
    g = [[] for i in range(n)]
    for i in range(n - 1):
        s, t, w = [int(v) for v in input().split()]
        g[s].append(Edge(t, w))
        g[t].append(Edge(s, w))
    solve(n, g)
