class Graph:
    def __init__(self):
        n, m = map(int, input().split())

        self.adj = [[] for _ in range(n)]
        for _ in range(m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            self.adj[a].append(b)
            self.adj[b].append(a)

        self.cnt = 0
        self.depth = 0
        self.ds = [-1] * n

    def solve(self, u):
        self.ds[u] = self.depth
        if self.ds.count(-1) == 0:
            self.cnt += 1
            return

        self.depth += 1
        for v in self.adj[u]:
            if self.ds[v] == -1:
                self.solve(v)
                self.ds[v] = -1
        self.depth -= 1


def main():
    graph = Graph()
    graph.solve(0)
    print(graph.cnt)


if __name__ == "__main__":
    main()
