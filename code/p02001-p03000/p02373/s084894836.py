import sys
from math import log2

sys.setrecursionlimit(int(1e7))


def doubling():
    dfs(0, -1, 0)
    p0 = parent[0]
    for p1 in parent[1:]:
        for i in range(n):
            pi = p0[i]
            p1[i] = -1 if pi < 0 else p0[pi]
        p0 = p1


def dfs(u, p, d):
    parent[0][u] = p
    depth[u] = d
    for v in tree[u]:
        dfs(v, u, d + 1)


def lca(u, v):
    du, dv = depth[u], depth[v]
    if du > dv:
        u, v = v, u
        du, dv = dv, du
    for i, p in enumerate(parent):
        if (dv - du) >> i & 1:
            v = p[v]
    if u == v:
        return u
    for p in parent[logn - 1:None:-1]:
        pu, pv = p[u], p[v]
        if pu != pv:
            u, v = pu, pv
    return parent[0][u]


n = int(input())
tree = [set(map(int, input().split()[1:])) for _ in range(n)]

logn = int(log2(n)) + 1
parent = [[0] * n for _ in range(logn)]
depth = [0] * n

doubling()

q = int(input())
for _ in range(q):
    print(lca(*map(int, input().split())))

