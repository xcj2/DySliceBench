import sys
inf = float('inf')

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def SSSP(n, Adj):
    d = [inf] * n
    p = [-1] * n
    checked = [False] * n
    d[0] = 0
    checked[0] = True
    u = 0

    for i in range(n - 1):
        for v, cost in Adj[u]:
            if d[u] + cost < d[v]:
                p[v] = u
                d[v] = d[u] + cost

        min_n = 0
        min_w = inf
        for v in range(n):
            if not checked[v] and d[v] < min_w:
                min_n = v
                min_w = d[v]

        u = min_n
        checked[u] = True

    return d

def solve():
    n = int(input())
    Adj = [[] for i in range(n)]

    for i in range(n):
        u, k, *line = [int(i) for i in input().split()]
        for j in range(k):
            Adj[u].append((line[2*j], line[2*j + 1]))

    # debug(Adj, locals())

    d = SSSP(n, Adj)

    for i in range(n):
        print(i, d[i])

if __name__ == '__main__':
    solve()