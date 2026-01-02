#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10 ** 6)

class Impossible(ValueError):
    pass

def main():
    n, m = map(int, input().split())
    lrds = []
    for i in range(m):
        l, r, d = map(int, input().split())
        lrds.append((l - 1, r - 1, d))

    adj = [[] for i in range(n)]
    parents = [i for i in range(n)]
    for i in range(m):
        l, r, d = lrds[i]
        union(parents, l, r)
        adj[l].append((r, d))
        adj[r].append((l, -d))

    ds = set()
    for i in range(n):
        ds.add(find(parents, i))

    pos = [None for i in range(n)]
    try:
        for i in ds:
            pos[i] = 0
            dfs(adj, pos, i)
        print("Yes")
    except Impossible:
        print("No")

def dfs(adj, pos, x):
    for y, d in adj[x]:
        if pos[y] is None:
            pos[y] = pos[x] + d
            dfs(adj, pos, y)
        elif pos[y] != pos[x] + d:
            raise Impossible

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, x, y):
    p[find(p, y)] = find(p, x)


main()
