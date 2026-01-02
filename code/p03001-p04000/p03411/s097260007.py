INF = 1000000007

class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class FF:
    def __init__(self, n):
        self.n = n
        self.adj = []
        for i in range(n):
            self.adj.append([])
        self.used = [False] * n

    def add_edge(self, _from, _to, _cap):
        self.adj[_from].append(Edge(_to, _cap, len(self.adj[_to])))
        self.adj[_to].append(Edge(_from, 0, len(self.adj[_from]) - 1))

    def dfs(self, v, t, f):
        if v == t:
            return f
        self.used[v] = True
        for e in self.adj[v]:
            if self.used[e.to] == False and e.cap > 0:
                d = self.dfs(e.to, t, min(f, e.cap))
                if d > 0:
                 e.cap -= d
                 self.adj[e.to][e.rev].cap += d
                 return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            del self.used
            self.used = [False] * self.n
            f = self.dfs(s, t, INF)
            if f == 0:
                return flow
            flow += f


def main():
    n = int(input())
    reds = [tuple(int(s) for s in input().split()) for _ in range(n)]
    blues = [tuple(int(s) for s in input().split()) for _ in range(n)]
    ff = FF(2 * n + 2)
    for i in range(n):
        ff.add_edge(2 * n, i, 1)
        ff.add_edge(i + n, 2 * n + 1, 1)
    for i, (rx, ry) in enumerate(reds):
        for j, (bx, by) in enumerate(blues):
            if rx < bx and ry < by:
                ff.add_edge(i, j + n, 1)
    print(ff.max_flow(2 * n, 2 * n + 1))


if __name__ == '__main__':
    main()
