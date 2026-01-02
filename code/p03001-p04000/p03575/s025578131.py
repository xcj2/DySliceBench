#!/usr/bin/env python3

from copy import deepcopy

def dfs(x, adj, visited):
    for y, flag in enumerate(adj[x]):
        if flag and not visited[y]:
            visited[y] = True
            dfs(y, adj, visited)

def is_simply_connected(adj):
    n = len(adj)
    visited = [(i == 0) for i in range(n)]
    dfs(0, adj, visited)
    return False not in visited

def main():
    n, m = map(int, input().split())
    adj = [[(i == j) for i in range(n)] for j in range(n)]
    edges = set()
    for i in range(m):
        a1, b1 = map(int, input().split())
        a = a1 - 1
        b = b1 - 1
        edges.add((a, b))
        adj[a][b] = True
        adj[b][a] = True

    res = 0
    for a, b in edges:
        adj[a][b] = adj[b][a] = False
        if not is_simply_connected(adj):
            res += 1
        adj[a][b] = adj[b][a] = True
    print(res)

main()
