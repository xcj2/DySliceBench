from math import log2


def build():
    global parent
    dfs()
    pk0 = parent[0]
    for pk1 in parent[1:]:
        for v in range(n):
            pkv = pk0[v]
            pk1[v] = -1 if pkv < 0 else pk0[pkv]
        pk0 = pk1


def dfs():
    global depth, parent, tree
    stack = [(0, -1, 0)]
    while stack:
        v, p, d = stack.pop()
        parent[0][v] = p
        depth[v] = d
        stack.extend((child, v, d + 1) for child in tree[v])


def lca(u: int, v: int) -> int:
    global depth, parent
    du, dv = depth[u], depth[v]
    if du > dv:
        u, v = v, u
        du, dv = dv, du
    for k, pk in enumerate(parent):
        if (dv - du) >> k & 1:
            v = pk[v]
    if u == v:
        return u
    for pk in parent[logn - 1:None:-1]:
        pku, pkv = pk[u], pk[v]
        if pku != pkv:
            u, v = pku, pkv
    return parent[0][u]


if __name__ == "__main__":
    n = int(input())
    tree = []
    for _ in range(n):
        _, *children = map(lambda x: int(x), input().split())
        tree.append(set(children))

    logn = int(log2(n)) + 1
    parent = [[0] * n for _ in range(logn)]
    depth = [0] * n
    build()

    q = int(input())
    for _ in range(q):
        u, v = map(lambda x: int(x), input().split())
        print(lca(u, v))

