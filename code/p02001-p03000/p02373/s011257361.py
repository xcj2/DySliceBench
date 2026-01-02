from math import log2


def build():
    dfs()
    pk0 = parent[0]
    for k in range(1, logn):
        pk1 = parent[k]
        for v in range(n):
            pkv = pk0[v]
            pk1[v] = -1 if pkv < 0 else pk0[pkv]
        pk0 = pk1


def dfs():
    stack = [(0, -1, 0)]
    while stack:
        v, p, d = stack.pop()
        parent[0][v] = p
        depth[v] = d
        stack.extend((child, v, d + 1) for child in tree[v])


def get(u, v):
    du, dv = depth[u], depth[v]
    if du > dv:
        u, v = v, u
        du, dv = dv, du
    for k in range(logn):
        if (dv - du) >> k & 1:
            v = parent[k][v]
    if u == v:
        return u
    for k in range(logn - 1, -1, -1):
        pk = parent[k]
        if pk[u] != pk[v]:
            u, v = pk[u], pk[v]
    return parent[0][u]


n = int(input())
tree = [set(map(int, input().split()[1:])) for _ in range(n)]

logn = int(log2(n)) + 1
parent = [[0] * n for _ in range(logn)]
depth = [0] * n
build()

q = int(input())
for _ in range(q):
    print(get(*map(int, input().split())))