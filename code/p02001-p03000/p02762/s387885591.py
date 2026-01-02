#!/usr/bin/env python3

import sys

def main():
    sys.setrecursionlimit(1000000)
    n, m, k = map(int, input().split())
    friends = [set() for i in range(n)]
    blocks = [set() for i in range(n)]
    parents = [i for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        friends[a - 1].add(b - 1)
        friends[b - 1].add(a - 1)
        unite(a - 1, b - 1, parents)
    for i in range(k):
        c, d = map(int, input().split())
        blocks[c - 1].add(d - 1)
        blocks[d - 1].add(c - 1)
    groups = [set() for i in range(n)]
    for i in range(n):
        p = find(i, parents)
        groups[p].add(i)
    res = []
    for i in range(n):
        p = find(i, parents)
        res.append(len(groups[p]) - len(friends[i]) - len(groups[p] & blocks[i]) - 1)
    print(" ".join([str(x) for x in res]))

def unite(x, y, parents):
    px = find(x, parents)
    py = find(y, parents)
    parents[py] = px

def find(x, parents):
    if parents[x] == x:
        return x
    fx = find(parents[x], parents)
    parents[x] = fx
    return fx

if __name__ == "__main__":
    main()
