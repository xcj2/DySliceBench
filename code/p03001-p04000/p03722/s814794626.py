import sys
from math import sqrt

inf = 1<<60

def solve():
    N, M = map(int, sys.stdin.readline().split())

    edges = [None] * M
    Adj = [[] for i in range(N)]
    Adjr = [[] for i in range(N)]

    for i in range(M):
        ai, bi, ci = map(int, sys.stdin.readline().split())
        edges[i] = (ai - 1, bi - 1, -ci)
        Adj[ai - 1].append(bi - 1)
        Adjr[bi - 1].append(ai - 1)

    visitable = [False] * N
    dfs(N, M, Adj, visitable, 0)

    reachable = [False] * N
    dfs(N, M, Adjr, reachable, N - 1)

    valid = [visitable[i] and reachable[i] for i in range(N)]

    edges = [(u, v, c) for (u, v, c) in edges if valid[u] and valid[v]]

    ans = BellmanFord(N, M, edges, valid)

    if ans is None:
        print('inf')
    else:
        print(-ans)

def dfs(N, M, Adj, visited, u):
    visited[u] = True

    for v in Adj[u]:
        if not visited[v]:
            dfs(N, M, Adj, visited, v)

def BellmanFord(N, M, edges, valid):
    d = [inf] * N
    d[0] = 0

    for i in range(N):
        flag = False

        for (u, v, c) in edges:
            if d[u] != inf and d[u] + c < d[v]:
                d[v] = d[u] + c
                flag = True

        if not flag:
            break

        if flag and i == N - 1:
            return None

    return d[N - 1]

if __name__ == '__main__':
    solve()