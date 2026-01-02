import sys
from collections import deque

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def bfs(n, adj):
    dis = [-1] * n
    visited = [False] * n
    nxt = deque([0])
    dis[0] = 0
    visited[0] = True

    while nxt:
        u = nxt.popleft()

        for v in adj[u]:
            if not visited[v]:
                dis[v] = dis[u] + 1
                visited[v] = True
                nxt.append(v)

    return dis

def solve():
    n = int(input())
    adj = [None] * n
    for i in range(n):
        u, k, *vs = [int(j) - 1 for j in input().split()]
        adj[u] = vs

    # debug(adj, locals())
    dis = bfs(n, adj)

    for i in range(n):
        print(i + 1, dis[i])

    pass

if __name__ == '__main__':
    solve()