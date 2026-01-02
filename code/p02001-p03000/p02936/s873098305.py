import sys


sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline().strip()


def solve():
    def dfs(v):
        for nv in g[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            counter[nv] += counter[v]
            dfs(nv)

    N, Q = map(int, input().split())
    g = [set() for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].add(b)
        g[b].add(a)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x

    visited = [False] * N
    visited[0] = True
    dfs(0)
    return counter


print(" ".join(map(str, solve())))
