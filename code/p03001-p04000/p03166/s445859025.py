import sys
sys.setrecursionlimit(100000)

from collections import defaultdict



class Graph:

    def __init__(self, N):
        self.graph = defaultdict(list)
        self.N = N
        self.memo = [-1] * (N+1)
        self.tovisit = set(range(1, N+1))

    def add_edge(self, x, y):
        self.graph[x].append(y)

    def _longest_path(self, node):
        if self.memo[node] == -1:
            res = 0
            for y in self.graph[node]:
                res = max(res, 1 + self._longest_path(y))

            self.memo[node] = res
            self.tovisit.discard(node)

        return self.memo[node]

    def longest_path(self):
        while self.tovisit:
            self._longest_path(self.tovisit.pop())

        res = 0
        for i in range(1, self.N+1):
            res = max(res, self.memo[i])

        return res


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
