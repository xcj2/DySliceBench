import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def bfs(adj, nxt, dis, sumi, kyori):
    nnxt = []
    for u in nxt:
        sumi[u] = True
        dis[u] = kyori

    for u in nxt:
        for v in adj[u]:
            if not sumi[v]:
                nnxt.append(v)

    return nnxt, kyori + 1

def solve():
    n = int(input())
    adj = [None] * n
    for i in range(n):
        u, k, *vs = [int(j) - 1 for j in input().split()]
        adj[u] = vs

    # debug(adj, locals())

    sumi = [False] * n
    dis = [-1] * n
    nxt = [0]
    kyori = 0

    while nxt:
        nxt, kyori = bfs(adj, nxt, dis, sumi, kyori)

    for i in range(n):
        print(i + 1, dis[i])

    pass

if __name__ == '__main__':
    solve()