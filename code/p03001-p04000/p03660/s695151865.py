import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def bfs(edges, n_nodes):
    visited = [None] * n_nodes
    visited[0] = "B"
    visited[-1] = "W"

    q = deque([0, n_nodes - 1])

    while q:
        i = q.popleft()

        for j in edges[i]:
            if visited[j] is None:
                visited[j] = visited[i]
                q.append(j)

    return visited


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    visited = bfs(edges, N)
    if visited.count("B") > visited.count("W"):
        print("Fennec")
    else:
        print("Snuke")


if __name__ == "__main__":
    main()
