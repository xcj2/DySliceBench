from collections import defaultdict
import sys
sys.setrecursionlimit(100005)

class Graph:
    def __init__(self, N):
        self.in_degree = [0] * (N+1)
        self.dist = [0] * (N+1)
        self.visited = [False] * (N+1)
        self.edges = defaultdict(list)
        self.N = N

    def add_edge(self, x, y):
        self.edges[x].append(y)
        self.in_degree[y] += 1

    def dfs(self, x):
        self.visited[x] = True
        for y in self.edges[x]:
            self.dist[y] = max(self.dist[y], self.dist[x] + 1)
            self.in_degree[y] -= 1
            if self.in_degree[y] == 0:
                self.dfs(y)

    def longest_path(self):
        for i in range(1, self.N+1):
            if not self.visited[i] and self.in_degree[i] == 0:
                self.dfs(i)

        ans = 0
        for i in range(1, self.N+1):
            ans = max(ans, self.dist[i])

        return ans


def main():
    N, M = map(int, input().split())
    graph = Graph(N)
    for _ in range(M):
        x, y = map(int, input().split())
        graph.add_edge(x, y)

    ans = graph.longest_path()
    print(ans)


if __name__ == "__main__":
    main()
